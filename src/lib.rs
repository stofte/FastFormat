use std::ptr;
use std::ffi::CString;
use json;

#[no_mangle]
pub extern "C" fn parse_string(input_json: *const u16, len: usize) -> *const i8 {
    let sliced = unsafe { std::slice::from_raw_parts(input_json, len) };
    let str = String::from_utf16(sliced).unwrap();
    let json_parsed = match json::parse(&str) {
        Ok(dat) => dat,
        Err(..) => return ptr::null()
    };
    let json_formatted = json::stringify_pretty(json_parsed, 4);
    CString::new(json_formatted).unwrap().into_raw()
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
