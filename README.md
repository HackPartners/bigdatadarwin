[![Build Status](https://travis-ci.org/grundleborg/darwinpush.svg?branch=master)](https://travis-ci.org/grundleborg/darwinpush)

# darwinpush

A python library for the National Rail Enquiries Darwin Push Port API. The purpose of this library
is to simplify developing python programs that make use of the Darwin Push Port API by taking care
of all the low level STOMP usage and allowing you just to write a listener class which receives
friendly, easy to use objects representing the different message types the Push Port sends out,
avoiding the need for dealing with a STOMP library and low-level bindings of the XML data received.

*This library is still in its early stages of development and so a lot of it is incomplete or not
safe to rely on yet. Use at your own risk.*

## Current state of development:
* The core STOMP client and message handling code is in place, although lacks proper connection
  management and error handling.

* The generated bindings for the Darwin XSDs are in place.

* The implementation of the friendly message classes is mostly complete. All of the message types except for the following are implemented, with some reasonable level of test coverage (although some rarer properties are not fully tested yet).
  * Train Status
  * Tracking ID (appears to be not yet in use in public Darwin)
  * Train Alert (appears to be not yet in use in public Darwin)

## How To Use
Devlopment is still in its early stages, so there's no easy "How To" just yet. If that's what you
are looking for, your best bet is probably to check back in a month or two once the project has
progressed a bit further. If that hasn't put you off though, you can see some vague clues as to
how to get started in example.py.

## Help
I can't really offer much in the way of support right now, because the library isn't finished!

## I want to Get Involved
Patches are welcome! However, given the early state of development, it's probably best to get in
touch with me before you start hacking on something to avoid duplication of work, or incompatible
changes.

## Release Roadmap
I'm aiming for a release that's pretty much usable for pretty much all the common cases by the end
of August 2015. However, my hacking priorities can change rapidly without warning, so don't consider
this to be guaranteed by any means.


