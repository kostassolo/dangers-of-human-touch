# The Dangers of Human Touch: Fingerprinting Browser Extensions through User Actions
Repository for the artifacts and  the  defense mechanism of the paper by Konstantinos Solomos, Panagiotis Ilia, Soroush Karami, and Jason Polakis.


Paper : (to appear) in Usenix 22'



### Demo
Visit the  [demo page](demo/demo___the_dangers_of_human_touch (1080p).mp4)


### Defense tool

We implemented a tool for extension developers that allows them to retroactively fortify their extensions against pages that simulate user actions.
Our tool is a function wrapper in JavaScript that verifies the user triggered events (e.g., click, doubleclick, mouseover, copy,paste,etc. ) origin by overriding the **adddEventListener**.

Developers can automatically inject the function wrapper  and ovewrite the content script  by running the following command.

`inject.py -i path_to_content_script`





