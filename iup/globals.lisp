(defpackage #:iup-global
  (:use #:common-lisp))

(in-package #:iup-global)

;;; https://www.tecgraf.puc-rio.br/iup/en/attrib/iup_globals.html

;;; IUP globals can be strings or pointers and some even act like
;;; functions with side effects so need special treatment

;;; general

language
version
copyright
driver

;;; system control

lockloop
exitloop
lasterror
utf8mode
utf8mode_file
defaultprecision
defaultdecimalsymbol
sb_bgcolor
showmenuimages
overlayscrollbar
globalmenu
globallayoutdlgkey
globallayoutresizekey
imageautoscale
imagesdpi
imagestockautoscale
imagestocksize
singleinstance

;;; system mouse and keyboard

cursorpos
mousebutton
shiftkey
controlkey
modkeystate
keypress
keyrelease
key
autorepeat
inputcallbacks
system
systemversion
systemlanguage
systemlocale
scrollbarsize
comctl32ver6
gtkversion
gtkdevversion
motifversion
motifnummber
computername
username
exefilename
gl_version
gl_vendor
gl_renderer
xservervendor
xvendorrelease

;;; screen information

fullsize
screensize
screendepth
screendpi
trucolorcanvas
dwm_composition
virtualscreen
monitorscount
monitorsinfo

;; system data

(defun hinstance () (iup-cffi::%iup-get-global "HINSTANCE"))
(defun dll-hinstance () (iup-cffi::%iup-get-global "DLL_HINSTANCE"))
(defun appshell () (iup-cffi::%iup-get-global "APPSHELL"))
(defun xdisplay () (iup-cffi::%iup-get-global "XDISPLAY"))
(defun xscreen () (iup-cffi::%iup-get-global "XSCREEN"))

;;; default attributes

dlgbgcolor
dlgfgcolor
menubgcolor
menufgcolor
txtbgcolor
txtfgcolor
txthlcolor
linkfgcolor

(defun default-font ())
(defun (setf default-font) (new-value))


defaultfont
defaultfontface
defaultfontsize
defaultfontstyle
defaultbuttonpadding
defaulttheme
