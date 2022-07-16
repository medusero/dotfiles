set encoding=UTF-8
set number
set relativenumber
set autoindent
set tabstop=4
set shiftwidth=4
set smarttab
set softtabstop=4
set mouse=a
set clipboard+=unnamedplus
set guifont=UbuntuMono\ Nerd\ Font:h7

call plug#begin()

Plug 'catppuccin/nvim', {'as': 'catppuccin'}
Plug 'itchyny/lightline.vim'
Plug 'https://github.com/ap/vim-css-color'
Plug 'lukas-reineke/indent-blankline.nvim'
Plug 'https://github.com/preservim/nerdtree'
Plug 'https://github.com/ryanoasis/vim-devicons'
Plug 'mg979/vim-visual-multi', {'branch': 'master'}
Plug 'jiangmiao/auto-pairs'
Plug 'tribela/vim-transparent'

call plug#end()

let g:catppuccin_flavour = "mocha"
colorscheme catppuccin
let g:lightline = {'colorscheme': 'catppuccin'}

let mapleader = ","

let NERDTreeShowHidden=1
let g:NERDTreeWinPos = "right"
nnoremap <C-f> :NERDTreeFocus<CR>
nnoremap <C-g> :NERDTree<CR>
nnoremap <C-t> :NERDTreeToggle<CR>
autocmd BufEnter * silent if winnr('$') == 1 && exists('b:NERDTree') && b:NERDTree.isTabTree() | quit | endif

let g:multi_cursor_start_word_key      = '<C-n>'
let g:multi_cursor_select_all_word_key = '<A-n>'
let g:multi_cursor_start_key           = 'g<C-n>'
let g:multi_cursor_select_all_key      = 'g<A-n>'
let g:multi_cursor_next_key            = '<C-n>'
let g:multi_cursor_prev_key            = '<C-p>'
let g:multi_cursor_skip_key            = '<C-x>'
let g:multi_cursor_quit_key            = '<Esc>'
