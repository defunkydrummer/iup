(defpackage #:iup-examples.detached
  (:use #:common-lisp)
  (:export #:detached))

(in-package #:iup-examples.detached)

(defun detached ()
  (iup:with-iup ()
    (let* ((button1 (iup:button :title "Detach Me!" :action 'button-detach-callback))
	   (multi-line (iup:multi-line :expand :yes :visiblelines 5))
	   (hbox (iup:hbox (list button1 multi-line) :margin "0x0"))
	   (dbox (iup:detach-box hbox :orientation :vertical :detached_cb 'detached-callback))
	   (label (iup:label :title "Label" :expand :vertical))
	   (button2 (iup:button :title "Restore me!" :expand :yes :active :no :action 'button-restore-callback))
	   (text (iup:text :expand :horizontal))
	   (dialog (iup:dialog (iup:vbox (list dbox label button2 text)
                                         :margin "10x10"
                                         :gap 10)
			       :title "IupDetachBox Example"
			       :rastersize "300x300")))
      (iup:show dialog)
      (iup:main-loop))))

#+sbcl
(sb-int:with-float-traps-masked
    (:divide-by-zero :invalid)
  (detached))
