//! The message protocol shared by the client and the server.
//!
//! A message is a fixed binary layout, so both ends always agree:
//!
//! ```text
//!   offset  size  field
//!   0       4     name length N          (u32, big-endian / network byte order)
//!   4       N     name                   (UTF-8 bytes)
//!   4 + N   2     integer                (u16, big-endian / network byte order)
//! ```
//!
//! Endianness: the integer travels as raw bytes, so the two ends must agree on
//! byte order.  We fix it to big-endian ("network byte order", the C `hton`/
//! `ntoh` convention) by using `to_be_bytes`/`from_be_bytes`.  That means a
//! little-endian client and a big-endian server interoperate with no
//! special-casing — this is exactly how real network protocols handle
//! endianness.  (A text/ASCII number would sidestep endianness entirely, at the
//! cost of sending more bytes.)
//!
//! The number is a `u16`: the assignment's 1..=100 fits with room for the
//! out-of-range values that trigger the server's "kill switch".  A single `u8`
//! byte would be smaller still, but it limits values to 0..=255.

use std::io::{self, Read, Write};

/// Largest name we'll accept, to avoid a huge allocation from a corrupt length.
const MAX_NAME_LEN: usize = 4096;

/// One message: a name and a number.
#[derive(Debug, Clone, PartialEq, Eq)]
pub struct Message {
    pub name: String,
     /// u16: 1..=100 fits, with room for out-of-range kill-switch values.
    pub number: u16,
}

impl Message {
     /// Write `self` to `writer` in the fixed big-endian layout above.
     /// (The C equivalent is `send()` of a packed `struct { char name[..]; int; }`.)
    pub fn write_to<W: Write>(&self, writer: &mut W) -> io::Result<()> {
        let name_bytes = self.name.as_bytes();
        writer.write_all(&(name_bytes.len() as u32).to_be_bytes())?; // 4-byte length, big-endian
        writer.write_all(name_bytes)?;                               // the name itself
        writer.write_all(&self.number.to_be_bytes())                 // 2-byte number, big-endian
     }

     /// Read exactly one message from `reader`, blocking until the full
     /// 4 + N + 2 bytes have arrived.  (The C equivalent is a `recv()` loop.)
    pub fn read_from<R: Read>(reader: &mut R) -> io::Result<Message> {
        let mut len_buf = [0u8; 4];
        reader.read_exact(&mut len_buf)?;
        let name_len = u32::from_be_bytes(len_buf) as usize;
        if name_len > MAX_NAME_LEN {
            return Err(io::Error::new(
                 io::ErrorKind::InvalidData,
                format!("name length {name_len} exceeds the {MAX_NAME_LEN}-byte limit"),
             ));
        }

        let mut name_buf = vec![0u8; name_len];
        reader.read_exact(&mut name_buf)?;

        let mut num_buf = [0u8; 2];
        reader.read_exact(&mut num_buf)?;

        Ok(Message {
            name: String::from_utf8_lossy(&name_buf).into_owned(),
             number: u16::from_be_bytes(num_buf),
        })
     }
}
