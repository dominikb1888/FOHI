//! `socketclient` — client half of Programming Assignment 1.
//!
//! Behaviour (from the assignment):
//!    * Read an integer 1..=100 from the keyboard.
//!    * Open a TCP connection to the server and send its name string
//!      ("Client of John Q. Smith") together with the integer.
//!    * Read the server's reply and display its own name, the server's name,
//!     both integers and their sum, then close its socket and exit.
//!
//! It is a separate binary, so the "wide" social part of the assignment is easy:
//! point it at another student's server with
//! `cargo run --bin socketclient -- <their.ip> <port>` (integer on stdin).
//!
//! The number is a raw 2-byte (u16, big-endian / network byte order) value, so
//! the client and server interoperate regardless of endianness.  See protocol.rs.
//!
//! Uses only `std::net`; no external crates.  The equivalent C socket calls are
//! written next to each step.
//!
//! Usage:  cargo run --bin socketclient -- [host] [port]
//!   NAME="Your Name" cargo run --bin socketclient -- 127.0.0.1 5001
//!   <enter your integer on stdin>

mod protocol;

use protocol::Message;
use std::io::Write;
use std::net::TcpStream;

const DEFAULT_HOST: &str = "127.0.0.1";
const DEFAULT_PORT: u16 = 5001;

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let host = args.get(1).map(String::as_str).unwrap_or(DEFAULT_HOST);
    let port: u16 = args
         .get(2)
         .and_then(|s| s.parse().ok())
         .unwrap_or(DEFAULT_PORT);

     // The client's name; override with NAME to put in your own.
    let person = std::env::var("NAME").unwrap_or_else(|_| "Student".to_string());
    let client_name = format!("Client of {person}");

     // 1.  Accept the integer 1..=100 from the keyboard.
    print!("[client] enter an integer 1..100 (out-of-range shuts the server down): ");
    std::io::stdout().flush().ok();
    let mut line = String::new();
    if std::io::stdin().read_line(&mut line).is_err() {
        eprintln!("[client] could not read from the keyboard");
        std::process::exit(1);
     }
      // The wire number is a u16, so 1..=100 fits with room for out-of-range
      // kill-switch values.  (A single u8 byte would be smaller still but caps
      // the value at 255.)
    let client_number: u16 = match line.trim().parse() {
        Ok(n) => n,
        Err(_) => {
            eprintln!("[client] \"{line}\" is not a number in 0..65535");
            std::process::exit(1);
          }
      };
    println!("[client] read integer {client_number} from the keyboard");

     // 2.  Open the connection.
     // C:  int c = socket(AF_INET, SOCK_STREAM, 0);
     //     connect(c, &addr, sizeof addr);
    let mut stream = match TcpStream::connect(format!("{host}:{port}")) {
        Ok(stream) => stream,
        Err(e) => {
            eprintln!("[client] socket()/connect() to {host}:{port} failed: {e}");
            std::process::exit(1);
          }
      };
    println!("[client] connect(): connected to {host}:{port} as \"{client_name}\"");

     // 3.  Send our name and number: raw big-endian integer on the wire.
     // C:  send(c, msg, len, 0);
    let request = Message {
         name: client_name.clone(),
         number: client_number,
     };
    if let Err(e) = request.write_to(&mut stream) {
        eprintln!("[client] send() failed: {e}");
        std::process::exit(1);
     }
    println!("[client] send(): sent \"{client_name}\" and number {client_number}");

     // 4.  Read the server's reply.
     // C:  recv(c, buf, len, 0);
    let reply = match Message::read_from(&mut stream) {
        Ok(reply) => reply,
        Err(_) => {
             // The server may have terminated (out-of-range number) without replying.
            println!("[client] the server closed the connection without replying \
                  (likely an out-of-range number that shut it down)");
            std::process::exit(0);
          }
      };
    let Message {
         name: server_name,
         number: server_number,
     } = reply;

     // 5.  Display everything and the sum the assignment asks for.
    let sum = (client_number as u32) + (server_number as u32);
    println!("[client] my name        = \"{client_name}\"");
    println!("[client] server name    = \"{server_name}\"");
    println!("[client] my number      = {client_number}");
    println!("[client] server number  = {server_number}");
    println!("[client] sum            = {sum}");

     // 6.  C:  close(c)   — `stream` is dropped at the end of main.
    println!("[client] close(): released socket; exiting");
}
