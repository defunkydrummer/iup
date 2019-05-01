(defpackage #:iup-examples.beep
  (:use #:common-lisp))

(in-package #:iup-examples.beep)

(defun beep ()
  (iup:with-iup ()
    (let* ((slider (iup:val :min 27.5 :max 4186 :expand :yes))
	   (left-button (iup:button :title "<"))
	   (frequency (iup:text :value 440))
	   (hz-label (iup:label :title "Hz"))
	   (right-button (iup:button :title ">"))
	   (hbox1 (iup:hbox (list left-button
				  frequency
				  hz-label
				  right-button)
			    :alignment :acenter))
	   (duration-label (iup:label :title "Duration"))
	   (duration (iup:text :value 200))
	   (ms-label (iup:label :title "ms"))
	   (play (iup:button :title "Play"))
	   (note-label (iup:label :title "♬"))
	   (note (loop with list = (iup:list)
		       for name in '("A1" "A2" "A3")
		       for i from 1
                       do (setf (iup:attribute list i) name)
		       finally (return list)))
	   (hbox2 (iup:hbox (list duration-label
				  duration
				  ms-label
				  play
				  note-label
				  note)
			    :alignment :acenter))
	   (vbox (iup:vbox (list slider
			         hbox1
			         hbox2)
			   :gap 10
			   :margin "10x10"
			   :alignment :acenter))
	   (dialog (iup:dialog vbox :title "Beep")))
      (iup:show dialog))
    (iup:main-loop)))

#-sbcl (beep)

#+sbcl
(sb-int:with-float-traps-masked
    (:divide-by-zero :invalid)
  (beep))
