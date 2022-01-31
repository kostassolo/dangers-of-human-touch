import re
import csv
import argparse

def readFile(path):
    file = open(path, "r")
    text = file.read()
    file.close()
    return text

def writeFile(path,text):
    file = open(path,"w")
    file.write(text)
    file.close()

def wrapperInject():
    return '''Events = new Set(['Keydown','Keyup','Keypress','Scroll','Mousewheel','Wheel','Doubleclick','Select','Click','Mousedown','Mouseup','Blur','Focus','Cut','Copy','Paste','Mouseenter','Mouseout','Mousemove','Mouseover'])
orig = EventTarget.prototype.addEventListener;
EventTarget.prototype.addEventListener = function(){
  if ( Events.has(arguments[0]) ){
    let handler = arguments[1]
    arguments[1] = function(){
       let event = arguments[0];
       //event's origin
       if (event.isTrusted == false)
         return;
       else
         return handler.apply(this,arguments)
     }
   }
  return orig.apply(this, arguments);

}
'''



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Tool injecting wrapper function in content script.')
    parser.add_argument('-i', '--input', type=str, nargs='?',help='content-script path')
    args = parser.parse_args()
    if not args.input:
        print (parser.print_help())
        exit(-1)
    input_file=args.input
    output_file=args.input
    text = readFile(input_file)
    wrapper = wrapperInject()
    text = wrapper + text
    writeFile(output_file,text)
    print("Updated content script : ",output_file)
