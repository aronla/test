(cua-mode t)
    (setq cua-auto-tabify-rectangles nil) ;; Don't tabify after rectangle commands
    (transient-mark-mode 1) ;; No region when it is not highlighted
    (setq cua-keep-region-after-copy t) ;; Standard Windows behaviour

(server-start)

(windmove-default-keybindings 'meta)

(setq ido-enable-flex-matching t
      ido-auto-merge-work-directories-length -1
      ido-create-new-buffer 'always
      ido-use-filename-at-point 'guess
      ido-everywhere t
      ido-default-buffer-method 'selected-window)

(ido-mode 1)

(put 'ido-exit-minibuffer 'disabled nil)
(when (require 'ido-ubiquitous nil t)
  (ido-ubiquitous-mode 1))

(require 'package)
(add-to-list 'package-archives
             '("elpy" . "http://jorgenschaefer.github.io/packages/") )

(add-to-list 'package-archives
             '("melpa" . "http://melpa.milkbox.net/packages/") t)


(menu-bar-mode -1)
(toggle-scroll-bar -1)
(tool-bar-mode -1)

(add-to-list 'default-frame-alist '(fullscreen . maximized))

(defun my-python-mode-hook () 
  (linum-mode 1)) 
(add-hook 'python-mode-hook 'my-python-mode-hook) 

(package-initialize)
(elpy-enable)
(elpy-use-ipython)
(setq elpy-rpc-backend "jedi")

(setq python-shell-interpreter "C:\\Users\\aron\\Anaconda\\python.exe"
       python-shell-interpreter-args
       "-i C:\\Users\\aron\\Anaconda\\Scripts\\ipython-script.py console --pylab=qt")

(define-key yas-minor-mode-map (kbd "C-c k") 'yas-expand)
(define-key global-map (kbd "C-c o") 'iedit-mode)
(define-key elpy-mode-map (kbd "<tab> <left>") 'elpy-nav-move-iblock-left)
(define-key elpy-mode-map (kbd "<tab> <right>") 'elpy-nav-move-iblock-right)
(define-key elpy-mode-map (kbd "<tab> <up>") 'elpy-nav-move-iblock-up)
(define-key elpy-mode-map (kbd "<tab> <down>") 'elpy-nav-move-iblock-down)
(define-key elpy-mode-map (kbd "C-M-<left>") 'elpy-nav-move-iblock-left)
(define-key elpy-mode-map (kbd "C-M-<right>") 'elpy-nav-move-iblock-right)
(define-key elpy-mode-map (kbd "C-M-<up>") 'elpy-nav-move-iblock-up)
(define-key elpy-mode-map (kbd "C-M-<down>") 'elpy-nav-move-iblock-down)
(define-key elpy-mode-map (kbd "C-c C-e") 'python-shell-send-region)


(global-set-key [C-tab] 'elpy-company-backend)


(eval-after-load "elpy"
  '(cl-dolist (key '("M-<up>" "M-<down>" "M-<left>" "M-<right>" "C-<left>" "C-<right>" "C-<up>" "C-<down>"))
     (define-key elpy-mode-map (kbd key) nil)))

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes (quote (tsdh-dark))))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )

;;; Aron-defined functions

(defun kill-whitespace ()
          "Kill the whitespace between two non-whitespace characters"
          (interactive "*")
          (save-excursion
            (save-restriction
              (save-match-data
		(if (looking-at "[ \t\n]")
                (progn
		  (re-search-forward "[ \t\r\n]+" nil t)
                  (replace-match "" nil nil))
		(
		  kill-word 1)
		)))))

(global-set-key [C-delete] 'kill-whitespace)

(fset 'eval-python-paragraph
      [?\M-x ?s ?e ?l ?e backspace backspace backspace backspace ?m ?a ?r ?k ?- ?p ?a ?r ?a tab return ?\C-  ?\C-c ?\C-e C-down])

(define-key elpy-mode-map (kbd "C-c C-r") 'eval-python-paragraph)



