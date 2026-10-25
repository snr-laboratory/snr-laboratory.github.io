---
title: Computing and coding
---

# Computing and coding

[How we work](/labrules/) / Computing and coding

We maintain a small, understandable working environment on Linux and macOS. Group members and coding agents should be able to find the same tools, reproduce the same commands, and understand the code that runs an experiment. The practices below are our defaults; record any project-specific requirements alongside the project.

**On this page:** [Applications](#applications) | [Language tools](#language-tools) | [Terminal and editors](#terminal-and-editors) | [SSH](#ssh) | [Remote sessions](#remote-sessions) | [Portable scripts](#portable-scripts) | [C and memory](#c-and-memory) | [Coding agents](#coding-agents)

## Applications

**Keep applications under `$HOME/Applications/`.** On macOS, `.app` bundles can live directly in this directory. On both platforms, keep downloaded source in `$HOME/Applications/src/` and install locally built programs into the `$HOME/Applications/` prefix.

```text
$HOME/Applications/
    bin/        command-line executables
    include/    installed headers
    lib/        installed libraries
    share/      installed data and documentation
    src/        source checkouts and unpacked releases
    appvenv/    Python environment for everyday tools
```

For a project using a conventional configure script:

```sh
./configure --prefix="$HOME/Applications"
make
make install
```

For a Makefile that exposes `PREFIX`, follow its installation instructions and use `make PREFIX="$HOME/Applications" install`. Different build systems spell the setting differently; keep the destination consistent.

:::commentary
**Know what is installed and where**

A user-owned prefix makes applications easy to inspect, replace, and reproduce without administrator access. Prefer an upstream download or a straightforward source build when available. Use the operating system's package manager for system dependencies and updates where appropriate, while keeping our working tools under our control.
:::

Put `$HOME/Applications/bin/` near the front of `PATH` in `~/.zshrc` or `~/.bashrc`, according to the interactive shell you use:

```sh
export PATH="$HOME/Applications/bin:$PATH"
```

Bash login shells read `~/.bash_profile` rather than `~/.bashrc`; have the former load the latter if needed. Check `command -v program` and `program --version` when a command resolves to an unexpected installation. Scripts and agents must select their tools explicitly rather than depend on interactive aliases.

## Language tools

**Install language tools locally and keep their locations predictable.**

- **Go:** install the upstream toolchain under `$HOME/Applications/` and set `GOPATH="$HOME/Applications/go"`. Add the toolchain's `bin/` and `$GOPATH/bin/` to `PATH`.
- **Rust:** use [rustup](https://rust-lang.github.io/rustup/) with its normal user directories, `$HOME/.rustup/` and `$HOME/.cargo/`. Load `$HOME/.cargo/env` when present.
- **Node.js:** use [nvm](https://github.com/nvm-sh/nvm) under `$HOME/.nvm/`; load its `nvm.sh` from the interactive shell configuration.

A shell setup for the language directories is:

```sh
export GOPATH="$HOME/Applications/go"
export PATH="$GOPATH/bin:$PATH"

if [ -r "$HOME/.cargo/env" ]; then
    . "$HOME/.cargo/env"
fi

export NVM_DIR="$HOME/.nvm"
if [ -s "$NVM_DIR/nvm.sh" ]; then
    . "$NVM_DIR/nvm.sh"
fi
```

:::commentary
**The compiler and its workspace are different**

[`GOPATH`](https://go.dev/wiki/GOPATH) holds Go's module cache and installed commands; it is separate from the Go toolchain itself. Likewise, [Cargo's home](https://doc.rust-lang.org/cargo/guide/cargo-home.html) contains tools and caches. These are useful, explicit language conventions. Keep their versions and project manifests recorded so another machine can reproduce the environment.
:::

### Python

**Use `$HOME/Applications/appvenv/` for everyday Python tools and agent scripts. Avoid Conda and additional environment managers.** Bootstrap the environment with an appropriate installed Python 3:

```sh
python3 -m venv "$HOME/Applications/appvenv"
"$HOME/Applications/appvenv/bin/python" -m pip install -r requirements.txt
"$HOME/Applications/appvenv/bin/python" script.py
```

The requirements file belongs to the project being installed. Use `python -m pip` through this explicit interpreter so installation and execution target the same environment. Record dependencies and versions in the repository. Coordinate changes to the shared environment; agents should not silently upgrade it to solve an unrelated task.

:::commentary
**An explicit interpreter survives a new shell**

Activating a virtual environment is convenient interactively, but an agent, cron job, or SSH command may start without it. The full interpreter path works in all of those contexts and avoids accidentally installing into or running the system Python.
:::

### IC design tools and Codex

Use [OpenICEDA](https://github.com/ymei/OpenICEDA) at `/opt/OpenICEDA` for the IC design toolchain. Load its environment in the shell where it is needed:

```sh
. /opt/OpenICEDA/env.sh
```

Its environment script may activate the toolchain's own Python environment. Continue to invoke `$HOME/Applications/appvenv/bin/python` explicitly for general Python work. Follow the repository's build instructions for its EDA tools and process design kits.

Install or update Codex with [`utils/install-codex.sh`](https://github.com/ymei/Infra-Mgmt/blob/main/utils/install-codex.sh) from [Infra-Mgmt](https://github.com/ymei/Infra-Mgmt). From a checkout, run:

```sh
sh utils/install-codex.sh
```

The installer defaults to `$HOME/Applications/bin/` and verifies the downloaded package checksum. Keep this installation method consistent across machines.

## Terminal and editors

**Learn the terminal's editing and history commands. Keep Vim and Neovim on a shared configuration.** Small conveniences used hundreds of times a day are worth setting up once.

### Readline and Zsh

Our `~/.inputrc` configures Bash and other applications that use GNU Readline:

```text
"\e[2~": quoted-insert
"\e[3~": delete-char

"\e[1~": beginning-of-line
"\e[4~": end-of-line

"\e[5~": history-search-backward
"\e[6~": history-search-forward

"\ep": history-search-backward
"\en": history-search-forward

"\e[A": previous-history
"\e[B": next-history
```

Reload it in Bash with `bind -f "$HOME/.inputrc"`, or start a new shell. **Zsh does not read `.inputrc`.** Put the corresponding bindings in `~/.zshrc`, after any shell framework or plugin setup:

```zsh
bindkey -e
bindkey '\ep' history-beginning-search-backward
bindkey '\en' history-beginning-search-forward
bindkey '^R' history-incremental-pattern-search-backward
```

Use these keys with the Emacs editing mode selected above:

- **Alt-P / Alt-N:** search backward or forward through commands starting with the text before the cursor. Type `ssh ` first, for example, to revisit SSH commands.
- **Ctrl-R:** search history interactively; type part of the command and press Ctrl-R again for another match.
- **Ctrl-A / Ctrl-E:** move to the beginning or end of the line.
- **Alt-B / Alt-F:** move backward or forward by a word.
- **Ctrl-K / Ctrl-Y:** cut to the end of the line, then paste the cut text back.
- **Ctrl-U:** clear the line in Zsh; in Bash/Readline, cut from the cursor back to the beginning.
- **Up / Down:** browse history normally; **Tab** completes a command or path.

:::commentary
**Search a prefix instead of scrolling**

Prefix history search retrieves the command you intended without stepping through everything you ran yesterday. [Readline](https://www.gnu.org/software/bash/manual/html_node/Searching.html) and Zsh expose it through different configuration files. If the terminal intercepts Alt, configure Option/Alt to send Meta/Esc, or press Esc followed by the letter. Home, End, and Page keys also depend on the terminal's escape sequences.
:::

### One Vim configuration

The following shared `~/.vimrc` retains our editing settings, with Vim-only initialization guarded for Neovim and the optional fzf path checked:

```vim
set nocompatible
if !has('nvim')
    source $VIMRUNTIME/vimrc_example.vim
    let &termencoding = &encoding
endif
set ignorecase
set smartcase
set smartindent
set tabstop=4
set shiftwidth=4
set expandtab
set nobackup
set noundofile
set encoding=utf8
set fileencodings=ucs-bom,utf-8,gb18030
" Wrap for display without inserting line breaks.
set wrap
set formatoptions-=tc
colorscheme elflord
filetype plugin on
filetype indent on
set mouse=
if isdirectory('/opt/local/share/fzf/vim')
    set rtp+=/opt/local/share/fzf/vim
endif

let java_highlight_java_lang_ids=1
let java_highlight_java_io=1
let java_highlight_functions="style"
let java_highlight_debug=1
let java_allow_cpp_keywords=1

syntax enable
```

Put this adapter in `$HOME/.config/nvim/init.vim` so both editors use the same setup:

```vim
set runtimepath^=~/.vim runtimepath+=~/.vim/after
let &packpath = &runtimepath
source ~/.vimrc
```

If `XDG_CONFIG_HOME` is set, use its `nvim/init.vim` instead. Keep editor settings in `.vimrc`; the adapter only connects Neovim to it.

:::commentary
**Share the setup, account for the differences**

Neovim supports Vimscript configuration, but some legacy settings, including [`termencoding`](https://neovim.io/doc/user/vim_diff/#vim-differences), have been removed. Guarding Vim-only initialization avoids startup errors. Four-space indentation and soft wrapping are editing defaults; follow an existing repository's conventions. `nobackup` and `noundofile` disable backup files and persistent undo, so save and commit work regularly.
:::

Press `i` to enter insert mode and Esc to return to normal mode. Useful normal-mode commands include `/pattern` to search, `n` / `N` for the next / previous match, `gg` / `G` for the start / end of the file, `ciw` to change a word, and `u` / Ctrl-R to undo / redo. Use `:w` to save and `:%s/old/new/gc` to review replacements one at a time.

## SSH

**Use SSH with public-key authentication for remote access and Git.** Register the public key with the service or in the server's `~/.ssh/authorized_keys`. Keep private keys on your own machine or hardware token, and verify a new server's host-key fingerprint through a trusted channel.

A supported YubiKey can hold an SSH authentication key. For a FIDO2-capable key and OpenSSH build, one option is:

```sh
ssh-keygen -t ed25519-sk -C "your-name@your-machine"
ssh-add "$HOME/.ssh/id_ed25519_sk"
ssh-add -l
```

Use a passphrase-protected Ed25519 software key when a hardware token is unavailable. Check the [YubiKey SSH documentation](https://developers.yubico.com/SSH/) for the supported FIDO2, PIV, and OpenPGP routes; they have different setup requirements. In particular, confirm that your macOS OpenSSH build supports FIDO2 before using `ed25519-sk`.

:::commentary
**One authentication agent**

An [SSH agent](https://man.openbsd.org/ssh-agent) makes keys available through `SSH_AUTH_SOCK`; hardware-backed keys still need their token. If using GPG's SSH support for an OpenPGP token, use its agent socket consistently. Check `ssh-add -l` before starting another agent or replacing the socket setting.
:::

### Connection reuse

Create a private directory for control sockets:

```sh
mkdir -p "$HOME/.ssh/sockets"
chmod 700 "$HOME/.ssh" "$HOME/.ssh/sockets"
```

Use an alias in `~/.ssh/config`, replacing the example host, login, and identity with your own:

```sshconfig
Host lab
    HostName host.example.org
    User your-login
    IdentityFile ~/.ssh/id_ed25519_sk
    IdentitiesOnly yes
    ForwardAgent yes
    ControlMaster auto
    ControlPersist 10m
    ControlPath ~/.ssh/sockets/%r@%h:%p
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

Connect with `ssh lab`. `ControlMaster` shares one authenticated connection across terminals, file transfers, and Git operations. `ControlPersist` keeps it available for ten minutes after the last session closes. `ssh -O check lab` checks the master; `ssh -O exit lab` closes the shared connection and its sessions. These options are documented in [`ssh_config`](https://man.openbsd.org/ssh_config).

### Agent and port forwarding

Our SSH configuration enables agent forwarding by default for lab connections, so the remote machine can authenticate onward using your local agent. Forwarding exposes an authentication socket; it does not copy the private key. Use `ssh -a lab` to disable forwarding for a particular connection. For a jump host, `ssh -J gateway.example.org lab` lets the local client authenticate directly to the destination.

:::commentary
**Agent forwarding carries authority**

A process with access to the forwarded socket can request authentication while the connection is available. Our normal lab connections enable forwarding; disable it when connecting to a machine you do not trust. With ControlMaster, agent-forwarding state belongs to the master connection; changing options may require closing that connection first. See [OpenSSH's forwarding guidance](https://man.openbsd.org/ssh#A).
:::

For a notebook or web service listening on the remote machine's loopback port 8888, forward it to your own loopback interface:

```sh
ssh -N -o ExitOnForwardFailure=yes \
    -L 127.0.0.1:8888:127.0.0.1:8888 lab
```

Then open `http://127.0.0.1:8888` locally. For the reverse direction, expose your local port 8000 on the remote machine's loopback port 9000:

```sh
ssh -N -o ExitOnForwardFailure=yes \
    -R 127.0.0.1:9000:127.0.0.1:8000 lab
```

`-L` listens locally; `-R` listens remotely. `-N` runs the tunnel without a shell. Keep the listener on `127.0.0.1` unless sharing it is intentional. A tunnel transports the connection; the service's normal authentication still applies. See the [`ssh` manual](https://man.openbsd.org/ssh) for forwarding details.

## Remote sessions

**Run remote terminal work inside tmux or Screen. Use noVNC when you need a graphical desktop.** Start the terminal session on the remote machine after connecting over SSH, then return to that same host and account when reconnecting.

:::commentary
**Keep the session with the computation**

A terminal multiplexer keeps shells, editors, and running commands available when a laptop disconnects. Detach before leaving and reattach later. The session still depends on the remote host staying up; use the appropriate scheduler or service manager for jobs that need unattended operation or restart handling.
:::

### tmux

Use [gpakosz's .tmux configuration](https://github.com/gpakosz/.tmux). On a new account without an existing tmux configuration, install it with:

```sh
git clone --single-branch https://github.com/gpakosz/.tmux.git "$HOME/.tmux"
ln -s "$HOME/.tmux/.tmux.conf" "$HOME/.tmux.conf"
cp "$HOME/.tmux/.tmux.conf.local" "$HOME/.tmux.conf.local"
```

Keep personal settings in `~/.tmux.conf.local`, leaving the upstream `.tmux.conf` available for updates. If a configuration already exists, merge the local settings into it. Our local prefix configuration is:

```tmux
# Use Ctrl-o as the only prefix.
#<<< YMei
set -gu prefix2
unbind C-o
unbind C-b
set -g prefix C-o
bind C-o send-prefix
#>>> YMei
```

**The prefix is Ctrl-o.** Press and release it, then press the command key. Start a named session with `tmux new -s work`; after detaching, use `tmux ls` to list sessions and `tmux attach -t work` to return.

- **Ctrl-o, c:** create a window.
- **Ctrl-o, n / p:** move to the next / previous window.
- **Ctrl-o, d:** detach while leaving the session running.
- **Ctrl-o, Ctrl-o:** send a literal Ctrl-o to the program inside tmux.

See the [tmux manual](https://man.openbsd.org/tmux) for session and key-binding commands.

### GNU Screen

Screen is also part of our setup. Use the following `~/.screenrc`:

```text
escape ^oo  # suggested binding for emacs users
nethack on

# kill startup message
startup_message off
# detach on hangup
autodetach on
# define a bigger scrollback, default is 100 lines
defscrollback 1024

# shell
#shell -bash

# putty bindings
#bindkey \"^[OC\" next
#bindkey \"^[OD\" prev

# An alternative hardstatus to display a bar at the bottom listing the
# windownames and highlighting the current windowname in blue. (This is only
# enabled if there is no hardstatus setting for your terminal)
hardstatus on
hardstatus alwayslastline
#hardstatus string "%h (%n.%t)%? users: %u%?"
#termcapinfo xterm*|rxvt* hs:ts=\E]2;:fs=^G:ds=\E]2;Screen^G
hardstatus string "%{.bW}%-w%{.rW}%n %t%{-}%+w %=%{..G} %h %D %Y/%m/%d %c"
altscreen on
```

Here, `escape ^oo` selects Ctrl-o as the prefix and `o` as the key that sends a literal Ctrl-o. Start a named session with `screen -S work`, list sessions with `screen -ls`, and reconnect with `screen -r work`.

Use **Ctrl-o, c** to create a window, **Ctrl-o, n / p** to change windows, and **Ctrl-o, d** to detach. In Screen, **Ctrl-o, o** sends a literal Ctrl-o. The configuration enables detach on hangup, 1,024 lines of scrollback, a window/status bar, and alternate-screen handling. See [Screen's command-character documentation](https://www.gnu.org/software/screen/manual/html_node/Command-Character.html) for the prefix syntax.

### Browser desktops with noVNC

**Use [noVNC](https://github.com/novnc/noVNC) for graphical remote work in a browser**, including EDA editors and waveform viewers. Open the noVNC address provided for the machine and connect to its desktop. Use the client's keyboard and clipboard controls when the browser intercepts a key combination or clipboard access needs an explicit action.

Use the lab's authenticated HTTPS endpoint when one is provided. If the noVNC gateway instead listens on the remote machine's loopback port 6080, an SSH tunnel makes that web endpoint available locally:

```sh
ssh -N -o ExitOnForwardFailure=yes \
    -L 127.0.0.1:6080:127.0.0.1:6080 lab
```

For that example, open `http://127.0.0.1:6080/vnc.html`. Use the actual gateway port and page path from the machine's setup.

:::commentary
**The browser is the desktop client**

[noVNC](https://novnc.com/info.html) connects the browser to a remote VNC server, using a WebSocket connection or proxy. The applications run on the remote machine. Reconnecting returns to the same desktop while that remote session remains running; a browser tab alone does not provide session persistence.
:::

## Portable scripts

**Write automation in POSIX `sh`. Use standard utilities before adding dependencies.** This applies to scripts written by people and agents; Bash or Zsh is fine as an interactive shell.

Use `#!/bin/sh`, quote path expansions, and rely on familiar tools such as `printf`, `test` / `[`, `find`, `grep`, `sed`, `awk`, `sort`, and `make`. Keep scripts compatible with the standard macOS and Linux versions of those tools.

- Use `.` to load a shell file; avoid Bash arrays, `[[ ... ]]`, process substitution, and `source` in portable scripts.
- Avoid assumptions such as GNU-only `sed -i` flags or `grep -P`; use a temporary output file when editing portably.
- Pass paths and arguments explicitly. Test scripts with `sh -n script.sh`, then exercise their actual success and failure paths.
- When Python is the clearer tool, invoke `$HOME/Applications/appvenv/bin/python` and use the standard library where practical.

:::commentary
**A small dependency chain is easier to maintain**

A short script built from standard tools is easy to run over SSH, inspect during a failure, and move between machines. Choose Python when parsing or state becomes awkward in shell. Keep the interpreter, inputs, and expected output clear in either case.
:::

### Repository-local scratch space

**Keep scratch space inside the repository. Never use system-wide directories such as `/tmp`, `/private/tmp`, or `/var/tmp`.** Use `build/` for temporary compilation output, `tmp/` for short-lived files, and `work/` for exploratory scripts, downloads, browser profiles, and screenshots. Add these directories to the repository's ignore rules.

Configure each tool's temporary, cache, and profile paths explicitly when needed. For tools that respect `TMPDIR`, for example:

```sh
mkdir -p tmp
TMPDIR="$PWD/tmp" "$HOME/Applications/appvenv/bin/python" script.py
```

For `mktemp`, supply a local template such as `"$PWD/tmp/task.XXXXXX"`. Keep scratch out of directories that are published or copied into a deliverable.

:::commentary
**Keep an experiment's working files together**

Local scratch stays with the checkout that created it. That makes intermediate results easier to inspect, avoids collisions between unrelated tasks, and gives cleanup a clear boundary. The same rule applies to agents: temporary scripts and browser artifacts belong with their task.
:::

## C and memory

**Strongly prefer C11 or later for compiled tools and firmware. Avoid introducing C++.** Favor small modules, explicit data structures, and direct control of memory. The [stb libraries](https://github.com/nothings/stb) and Tsoding's [nob.h](https://github.com/tsoding/nob.h) and [arena](https://github.com/tsoding/arena) illustrate the style we prefer.

- When a single-header library is appropriate, use an `*_IMPLEMENTATION` macro and define it in exactly one translation unit.
- Represent dynamic arrays with an explicit struct containing an element pointer, count, and capacity. Keep ownership, growth, and failure behavior visible.
- Group allocations by lifetime in an arena. Reset or release the arena when the whole group of objects is finished, instead of scattering `malloc` / `free` pairs throughout the code.
- Check allocation sizes, capacity growth, alignment, and failure paths. Keep interfaces and dependencies small enough to read and test.

A dynamic array makes its state explicit:

```c
typedef struct {
    Sample *items;
    size_t count;
    size_t capacity;
} Samples;
```

**For embedded and MCU acquisition code, plan memory before acquisition starts.** Prefer fixed buffers or arenas backed by a bounded memory region. Reserve storage during initialization and avoid heap allocation in interrupts and time-critical acquisition loops. Define what happens when a buffer fills or an arena runs out.

:::commentary
**Memory lifetime is part of the instrument**

Scattered allocation makes ownership harder to audit and can introduce fragmentation and unpredictable timing. An arena makes the lifetime of a run, event, or processing stage explicit. A reset invalidates every pointer into that region: wait until DMA, interrupt handlers, and other tasks have finished using it. Arrays that grow inside an arena can also leave old storage behind until reset; reserve capacity when the required bound is known.
:::

Compile with warnings enabled, for example `-std=c11 -Wall -Wextra -Wpedantic`. Exercise parsing, buffer boundaries, and allocation failures on the host, using sanitizers where supported, before relying on the code in an instrument. Keep compiler versions and build commands recorded in the project.

## Coding agents

**Use coding agents as part of an accountable engineering workflow. You own the resulting code and its behavior.** Give the agent a concrete goal, relevant files, constraints, and a way to check success. Make its working environment as explicit as your own.

### Copyable agent instructions

Paste this block into a CLI agent session, then describe the task and its acceptance criteria. It includes the working conventions without requiring the agent to read this page.

```text
Follow these working conventions for this task.

Tools and environment
- Read the repository's AGENTS.md and build instructions first.
  Inspect git status and preserve existing, unrelated changes.
- Prefer existing tools under $HOME/Applications and
  /opt/OpenICEDA before adding dependencies. Prefer upstream downloads
  or source builds over adding package-manager dependencies. Keep
  source in $HOME/Applications/src and install with a prefix of
  $HOME/Applications. Do not silently install or upgrade tools.
- Run Python explicitly as "$HOME/Applications/appvenv/bin/python".
  Use that interpreter's -m pip for package operations. Avoid Conda.
  Do not silently change the shared environment or substitute system
  Python if the environment is missing; report what is needed.
- Go uses GOPATH=$HOME/Applications/go. Rust uses $HOME/.cargo and
  $HOME/.rustup; Node.js uses $HOME/.nvm. Select tools explicitly
  rather than relying on interactive aliases or shell startup files.
- For IC design, use /opt/OpenICEDA and its env.sh as needed. Keep
  using the explicit appvenv interpreter for general Python work.

Portable scripts
- Write shell automation for POSIX sh with #!/bin/sh, not Bash.
  Quote paths and arguments. Avoid Bash arrays, [[ ... ]], process
  substitution, and source; use the POSIX dot command instead.
- Prefer standard tools such as printf, test, find, grep, sed, awk,
  sort, and make. Avoid GNU-only assumptions on macOS. Use Python's
  standard library when shell parsing becomes unnecessarily complex.

Scratch space
- Keep all scratch, temporary builds, downloads, generated helpers,
  browser profiles, caches for the task, and screenshots inside this
  repository's build/, tmp/, or work/. Add appropriate ignore rules.
- Never use system-wide scratch such as /tmp, /private/tmp, or
  /var/tmp. Set TMPDIR to an absolute repository-local path and
  configure tool-specific temporary, cache, and profile paths too.
  Give mktemp an explicit local template. Keep scratch out of
  published assets and deliverables.

C and memory
- Strongly prefer C11 or later for new compiled tools and firmware;
  avoid C++. Respect an existing project's required language.
- Use STB-style single-header libraries where appropriate, with each
  implementation macro defined in exactly one translation unit.
- Use explicit dynamic-array structs with items, count, and capacity.
  Prefer arenas with clear lifetimes over scattered malloc/free.
- Check sizes, alignment, capacity growth, and allocation failures.
  Reset arenas only after all users of their contents have finished.
- For embedded/MCU code, reserve bounded storage before acquisition.
  Avoid heap allocation in interrupts and time-critical loops, and
  define how buffer exhaustion is handled.

Verification and handoff
- Keep the change focused and review the final diff and dependencies.
  Run the documented build and relevant checks; check POSIX scripts
  with sh -n and exercise their success and failure paths.
- Report what changed, commands actually run, results, and anything
  still unverified. Keep durable rules in AGENTS.md and task-specific
  plans in separate files. Do not put credentials in commits or prompts.
```

### Working pattern

1. **Read first.** Inspect the repository instructions, existing code, and working-tree changes. Reproduce a problem before choosing a fix.
2. **State the environment.** Use POSIX `sh`, standard utilities, and the explicit `appvenv` interpreter. Follow the project's language, memory, and dependency conventions.
3. **Keep instructions durable.** Put stable repository rules in `AGENTS.md`; keep task plans and longer design notes in separate files. Record build and test commands where future contributors can find them.
4. **Review a focused change.** Read the diff, understand the implementation, and check new dependencies. Keep unrelated edits separate and preserve work already in progress.
5. **Verify behavior.** Run the relevant build and tests. For a defect, check that the original failure is fixed. Report the commands run, their results, and anything still unverified.
6. **Leave a useful record.** Commit coherent changes and document decisions, tool versions, and reproduction steps in the repository. Keep credentials and private keys out of commits and prompts; handle unpublished research data according to the lab's access rules.

:::commentary
**A working command is evidence**

An agent's explanation is useful, but confidence comes from a reproducible build, a test that exercises the relevant behavior, and a diff you can understand. For experimental software, also check units, calibration, timing, and failure behavior against the actual system. Fast implementation is valuable when it produces work that another researcher can verify and maintain.
:::

Keep improving this guide as the working environment changes. Bring questions and proposed refinements back to [How we work](/labrules/) and the group.
