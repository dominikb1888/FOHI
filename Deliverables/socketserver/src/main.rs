//! `socketserver` — server half of Programming Assignment 1.
//!
//! Behaviour (from the assignment):
//!    * Build its name string, e.g. "Server of John Q. Smith".
//!    * Accept connections.  For each client it prints the client's name and its
//!     own, picks an integer in 1..=100, prints the two numbers and their sum,
//!     and sends its name and number back.
//!    * If a client's integer is out of 1..=100 it terminates after releasing its
//!     sockets — the "kill switch".
//!
//! The number is a raw 2-byte (u16, big-endian / network byte order) value, not
//! ASCII text, so it costs fewer bytes than a text number and works even when
//! client and server have different endianness.  See `protocol.rs`.
//!
//! Uses only `std::net`; no external crates.  The equivalent C socket calls are
//! written next to each step so the classic C API stays visible.
//!
//! Usage:  cargo run --bin socketserver [-- [port]]
//!   NAME="Your Name" cargo run --bin socketserver -- 5001

mod protocol;

use protocol::Message;
use std::net::{TcpListener, TcpStream};

/// Default port.  Chosen > 1023 (and > 5000) as the assignment advises.
const DEFAULT_PORT: u16 = 5001;

fn main() {
     // The port is optional; defaults to DEFAULT_PORT so the server always starts.
    let port: u16 = std::env::args()
         .nth(1)
         .and_then(|s| s.parse().ok())
         .unwrap_or(DEFAULT_PORT);

     // The server's name.  Override with the NAME environment variable so a
     // student can drop in their own name without editing the source.
    let person = std::env::var("NAME").unwrap_or_else(|_| "Student".to_string());
    let server_name = format!("Server of {person}");

     // "It's fine for the server to use the same number all the time."
    const SERVER_NUMBER: u16 = 42;

    println!("[server] server name    = \"{server_name}\"");
    println!("[server] server number  = {SERVER_NUMBER}");

     // C:  int s = socket(AF_INET, SOCK_STREAM, 0);
     //     bind(s, &addr, sizeof addr);      // 0.0.0.0 on `port`
     //     listen(s, BACKLOG);
    let listener = match TcpListener::bind(format!("0.0.0.0:{port}")) {
        Ok(listener) => listener,
        Err(e) => {
            eprintln!("[server] socket()/bind()/listen() on 0.0.0.0:{port} failed: {e}");
            std::process::exit(1);
         }
     };
    println!("[server] listening on 0.0.0.0:{port}  (an out-of-range integer shuts it down)");

    loop {
         // C:  int c = accept(s, 0, 0);      // block until a client connects
        let (mut stream, peer) = match listener.accept() {
            Ok(pair) => pair,
            Err(e) => {
                eprintln!("[server] accept() failed: {e}");
                break;
             }
         };
        println!("[server] accept(): client connected from {peer}");

         // serve_one returns false on the out-of-range "kill switch".
        if !serve_one(&mut stream, &server_name, SERVER_NUMBER) {
            println!("[server] closing listening socket and terminating");
            break;
         }
     }
     // `listener` is dropped here, releasing the listening socket.
}

/// Serve one accepted client.  Returns `true` to keep serving, `false` to stop.
fn serve_one(stream: &mut TcpStream, server_name: &str, server_number: u16) -> bool {
     // C:  recv(c, buf, len, 0)   — read the client's message (name + raw integer).
    let client = match Message::read_from(stream) {
        Ok(message) => message,
        Err(e) => {
            eprintln!("[server] recv() failed: {e}; releasing this client's socket");
             // `stream` is released when the caller drops it.
            return true;
         }
     };
    let Message {
         name: client_name,
         number: client_number,
     } = client;

    println!("[server] received from \"{client_name}\": number {client_number}");

     // The assignment's "kill switch".
    if client_number < 1 || client_number > 100 {
        println!("[server] out-of-range number {client_number}; releasing sockets and terminating");
         // `stream` is released when the caller drops it after we return.
        return false;
     }

    let sum = (client_number as u32) + (server_number as u32);

     // The output the assignment asks for.
    println!("[server] client name    = \"{client_name}\"");
    println!("[server] server name    = \"{server_name}\"");
    println!("[server] client number  = {client_number}");
    println!("[server] server number  = {server_number}");
    println!("[server] sum            = {sum}");

     // C:  send(c, reply, len, 0)   — reply "servername" + raw integer.
    let reply = Message {
         name: server_name.to_string(),
         number: server_number,
     };
    if let Err(e) = reply.write_to(stream) {
        eprintln!("[server] send() failed: {e}");
     } else {
        println!("[server] send(): replied \"{server_name}\" with {server_number}");
     }

     // C:  close(c)   — `stream` is dropped when the caller's loop iteration ends.
    println!("[server] released client socket; waiting for the next client");
    true
}
