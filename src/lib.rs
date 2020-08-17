use std::{ptr, iter};
use std::io::Cursor;
use std::ffi::CString;
use json;
use quick_xml::{Reader, Writer};
use quick_xml::events::{Event, BytesEnd, BytesStart};

fn parse_json(input: &str) -> Option<String> {
    match json::parse(&input) {
        Ok(dat) => {
			let json_formatted = json::stringify_pretty(dat, 4);
			Some(json_formatted)
		},
        Err(..) => None
    }
}

fn parse_xml(input: &str) -> Option<String> {
    let mut reader = Reader::from_str(&input);
	reader.trim_text(true);
	let mut writer = Writer::new_with_indent(Cursor::new(Vec::new()), ' ' as u8, 4);
	let mut buf = Vec::new();
	loop {
		match reader.read_event(&mut buf) {
			Ok(Event::Eof) => break,
			Ok(e) => assert!(writer.write_event(e).is_ok()),
			Err(e) => panic!("Error at position {}: {:?}", reader.buffer_position(), e),
		}
		buf.clear();
	}
	Some(String::from_utf8(writer.into_inner().into_inner()).unwrap())
}

fn wrap_ptr(input: &str) -> *const i8 {
	CString::new(input).unwrap().into_raw()
}

#[no_mangle]
pub extern "C" fn parse(input: *const u16, len: usize) -> *const i8 {
    let sliced = unsafe { std::slice::from_raw_parts(input, len) };
    let utf16 = String::from_utf16(sliced).unwrap();
	match parse_json(&utf16) {
		Some(json) => wrap_ptr(&json),
		None => match parse_xml(&utf16) {
			Some(xml) => wrap_ptr(&xml),
			None => ptr::null()
		}
	}
}

#[no_mangle]
pub extern "C" fn free(ptr: *mut i8) {
    unsafe {
        if ptr.is_null() {
            return;
        }
        CString::from_raw(ptr);
    }
}
