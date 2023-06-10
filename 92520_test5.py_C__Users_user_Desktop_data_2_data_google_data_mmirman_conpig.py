#   Copyright 2013 Matthew Mirman
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import conpig

##################
##  TESTING IT  ##
##################

def test1(arg):
    for i in range(0,5):
        conpig.sleep(1)
        print arg
    raise Hello    

def test2(arg):
    for i in range(0,10):
        conpig.sleep(1)
        print arg
        

conpig.spawn(test1, "X")    
conpig.spawn(test2, "H")    
test2("O")


conpig.wait_all()
