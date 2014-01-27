"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from flash import Flash

flash_algo = { 'load_address' : 0x20000000,
               'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 
    0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770ba40, 0x4770bac0, 0x4770bac0, 
    0x4770bac0, 0x4770bac0, 0x4770bac0, 0x4770bac0, 0x4770bac0, 0x4770bac0, 0x4770bac0, 0x4770bac0, 
    0x4770bac0, 0x4770bac0, 0x4770bac0, 0x4770bac0, 0xb510492d, 0x60084449, 0xf24c482c, 0x81c15120, 
    0x1128f64d, 0x880181c1, 0x101f021, 0x48288001, 0xf0004448, 0x2800f8d5, 0x2001d000, 0x2000bd10, 
    0x460a4770, 0x48224601, 0x2300b510, 0xf0004448, 0x2800f9c1, 0x2001d000, 0xb57fbd10, 0x4605460c, 
    0xa9032000, 0x100e9cd, 0x48199002, 0x46224613, 0x44484629, 0xf9f0f000, 0x9803b110, 0xbd70b004, 
    0xe7fb1928, 0xb5104812, 0xf0004448, 0x2800f865, 0x2001d000, 0x490ebd10, 0x4449b510, 0x460168ca, 
    0x4448480b, 0xf82ef000, 0xd0002800, 0xbd102001, 0x4601460b, 0xb5104806, 0xf0004448, 0x2800f93d, 
    0x2001d000, 0xbd10, 0x4, 0x40052000, 0x8, 0x2170480a, 0x21807001, 0x78017001, 
    0xd5fc0609, 0x6817800, 0x2067d501, 0x6c14770, 0x2068d501, 0x7c04770, 0x2069d0fc, 0x4770, 
    0x40020000, 0x41f0e92d, 0x460d4614, 0xf886f000, 0xd11b2800, 0x1e64442c, 0xd0050521, 0xeb012101, 
    0x1e423114, 0x3401eb02, 0x447e4e09, 0x8024f8df, 0x42a52709, 0x6830d80a, 0xf8886005, 0xf7ff7007, 
    0x2800ffc9, 0xf505d102, 0xe7f25580, 0x81f0e8bd, 0x3be, 0x40020000, 0x4903b120, 0x71c82044, 
    0xbfb8f7ff, 0x47702004, 0x40020000, 0x4903b120, 0x71c82049, 0xbfaef7ff, 0x47702004, 0x40020000, 
    0xb132b138, 0xd2102905, 0xf001e8df, 0xb090905, 0x2004000d, 0x68c04770, 0x20006010, 0x68404770, 
    0x6880e7fa, 0x6800e7f8, 0x206ae7f6, 0x4770, 0xb161b168, 0x78804809, 0x203f000, 0xd0082a02, 
    0xebb22202, 0xd1061f90, 0x70082001, 0x2004e004, 0x20004770, 0x700ae7f9, 0x47702000, 0x40020000, 
    0x4a19b1b0, 0x4b196cd1, 0x6103f3c1, 0xf833447b, 0x3091011, 0x2300d00e, 0x3100e9c0, 0xf096cd1, 
    0x2101d00a, 0xf44f6081, 0x60c15180, 0x47702000, 0x47702004, 0x47702064, 0xe7f32102, 0xea41b128, 
    0x75b0302, 0x2065d003, 0x20044770, 0x68034770, 0xd804428b, 0x44116840, 0x42884418, 0x2066d201, 
    0x20004770, 0x4770, 0x40048000, 0x2dc, 0x45f0e92d, 0x1eb0a9, 0x460d4617, 0xd00b4604, 
    0xffdcf7ff, 0xd1082800, 0xeb056861, 0xf5b10807, 0xd9054f00, 0xe005094b, 0xb0292004, 0x85f0e8bd, 
    0x6380f44f, 0x22006824, 0x10dea4f, 0x4702fb03, 0x7022f841, 0x2a201c52, 0x2200d9f8, 0xa094f8df, 
    0xe001ac21, 0xd2082a08, 0xc010f89a, 0xfc02fa2c, 0xc01f00c, 0xc002f804, 0xf1a2e016, 0x2f080708, 
    0xf89ad202, 0xe00ac011, 0x710f1a2, 0xd2022f08, 0xc012f89a, 0xf89ae003, 0xf1a2c013, 0xfa2c0718, 
    0xf00cfc07, 0x54a70701, 0x2a201c52, 0x2200d3da, 0x46174694, 0xe01046a2, 0x4022f851, 0xd80b42ac, 
    0x482eb01, 0x42ac6864, 0xf81ad906, 0xf10c4002, 0xb9040c01, 0x441d1c7f, 0x45451c52, 0xb11fd3ec, 
    0xd1034567, 0xe0022101, 0xe0002100, 0x70312102, 0xe7a3, 0x40020000, 0x47f0e92d, 0x14461d, 
    0xd01e460e, 0xf7ff461a, 0x2800ff69, 0x4f0ed11a, 0xf8df447f, 0xf04fa038, 0x2d000807, 0x6838d012, 
    0x68396006, 0x60486820, 0x68606839, 0x60883408, 0x8007f88a, 0xfeaef7ff, 0xd1032800, 0x3d083608, 
    0x2004e7eb, 0x87f0e8bd, 0x198, 0x40020000, 0xb1d1b1d8, 0x20004a0e, 0xf0037893, 0x2b020303, 
    0x2045d014, 0x780871d0, 0x784872d0, 0x78887290, 0x78c87250, 0x79087210, 0x794873d0, 0x79887390, 
    0x79c87350, 0xf7ff7310, 0x2004be85, 0x4770, 0x40020000, 0x47f0e92d, 0x4614469a, 0x4605460e, 
    0xff1cf7ff, 0xd1252800, 0x101e9d5, 0xf8f1fbb0, 0xf1c84271, 0x40010000, 0x42b5424d, 0x4445d100, 
    0x1bafb1bc, 0xd90042a7, 0x480b4627, 0x44780939, 0x60066800, 0x22014809, 0xa0a71c2, 0x728172c2, 
    0xa009f880, 0xfe56f7ff, 0xd1032800, 0x443e1be4, 0x2000e7e5, 0x87f0e8bd, 0xda, 0x40020000, 
    0x4804b128, 0x71c22240, 0xf7ff7181, 0x2004be43, 0x4770, 0x40020000, 0x4df0e92d, 0xe9dd001c, 
    0x46168709, 0xd025460d, 0xfed8f7ff, 0xd11f2800, 0xb04cf8df, 0xf8df44fb, 0x2e00a04c, 0xf8dbd018, 
    0x600d1000, 0xf88a2202, 0x9a082007, 0x200bf88a, 0xf8db, 0x60816821, 0xfe1cf7ff, 0xf1b8b160, 
    0xd0010f00, 0x5000f8c8, 0xd0012f00, 0x60392100, 0x8df0e8bd, 0xe7fb2004, 0x1d241f36, 0xe7dc1d2d, 
    0x74, 0x40020000, 0xfffffffe, 0x0, 0x80000, 0x100000, 0x200000, 0x400000, 
    0x800000, 0x1000000, 0x1000000, 0x40020004, 0x0, 0x0, 
                                ],
               'pc_init' : 0x20000091,
               'pc_eraseAll' : 0x20000105,
               'pc_erase_sector' : 0x20000117,
               'pc_program_page' : 0x20000131,
               'begin_stack' : 0x20001000,
               'begin_data' : 0x20002000,
               'static_base' : 0x20000578,
               'page_size' : 4096
              };

memoryMapXML =  """
<?xml version="1.0"?>
<!DOCTYPE memory-map PUBLIC "+//IDN gnu.org//DTD GDB Memory Map V1.0//EN" "http://sourceware.org/gdb/gdb-memory-map.dtd">
<memory-map>
    <memory type="flash" start="0x0" length="0x100000"> <property name="blocksize">0x1000</property></memory>
    <memory type="ram" start="0x1ffe0000" length="0x40000"> </memory>
</memory-map>
"""


class Flash_k64f(Flash):
    
    def __init__(self, target):
        Flash.__init__(self, target, flash_algo, memoryMapXML)
    
