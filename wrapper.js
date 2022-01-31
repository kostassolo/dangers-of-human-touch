// All the mouse and key events
Events = new Set(['Keydown','Keyup','Keypress','Scroll','Mousewheel','Wheel','Doubleclick','Select','Click','Mousedown','Mouseup','Blur','Focus','Cut','Copy','Paste','Mouseenter','Mouseout','Mousemove','Mouseover'])
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
