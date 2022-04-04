# UMich ULCS Course Monitor

## About

With the [Two Course Limit](https://cse.engin.umich.edu/academics/for-current-students/advising/enrollment/) rules for UMich EECS Upper Level courses, if you want to enroll in more than two ULCS courses, you had better pay attention to whether the third one has its waitlist open so that you can get in the list early enough. This script is designed to monitor the open seats of the ULCS courses you want to enroll in. As soon as the available seats become 0 for any lecture or lab session, it will send a notification email.

## Getting Started

- Install `bs4`
    ```bash
    $ pip3 install bs4
    ```

- Configure `SENDER_EMAIL`, `SENDER_PASSWORD`, `RECEIVER_EMAIL`, and `UPDATE_INTERVAL` in `monitor.py`.

- Add the courses you want to monitor in `main()`. For example, EECS 482:

    ```python
    Monitor(482)
    ```

- Run the script

    ```bash
    $ python3 monitor.py
    ```

- To exit, press `Ctrl+C`.

    - If the process failed to exit properly, refer to [this link](https://superuser.com/questions/446808/how-to-manually-stop-a-python-script-that-runs-continuously-on-linux).

## Deployment on CAEN

***Update:** The following approach is **NOT** feasible. CAEN ssh service is not intended for long running jobs. The socket will be killed on the server side after a certain time. Please deploy the program on your virtual machine.*

Not all of us have a server available or a laptop running all day long. Deploying the program on [CAEN](https://caen.engin.umich.edu/connect/linux-login-service/) is then a good choice.

- First, connect to CAEN's Linux Remote Login Service using Secure Shell (SSH). To make it easier for future login without typing out the uniqname, hostname and using DUO every time, we can write these info in a config file. Edit the file with the path `~/.ssh/config` by appending the lines below.

  ```
  Host caen login.engin.umich.edu
          HostName login.engin.umich.edu
          User YOUR_UNIQ_NAME
          ControlMaster auto
          ControlPath ~/.ssh/_%r@%h:%p
          ControlPersist 0
  ```

  By setting up multiplexing, we can save our ssh control socket in the path specified by `ControlPath`, in this case, `~/.ssh`. Setting `ControlPersist` to 0 means the master connection will remain in the background indefinitely. Check the manual [here](https://man.openbsd.org/ssh_config.5).

- Then, connect to CAEN

  ```bash
  $ ssh caen
  ```

- `git clone` the project and follow the configuration above.

## Deployment on Virtual Machine

Another choice is to deploy the program on a virtual machine. Popular service providers include [Microsoft Azure Student](https://azure.microsoft.com/en-us/free/students/) and [Amazon AWS Educate](https://aws.amazon.com/education/awseducate/). Given the free credits for students, we can establish a virtual machine for free.

## Using `tmux` to Keep Processes Running

We will use `tmux` to run the program so that it will continue running after the ssh session disconnects. Learn more about other [approaches](https://unix.stackexchange.com/questions/479/keep-processes-running-after-ssh-session-disconnects) and a beginner [guide](https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/) to `tmux`.

- On CAEN or your virtual machine, start `tmux` with a new session

  ```bash
  $ ssh azure
  $ tmux
  ```

  Note: `tmux` should have been installed on CAEN.

- Run the program in the session

  ```bash
  $ python3 monitor.py
  ```

- Detach from the session by pressing `C-b d`, which means press `Ctrl+b`, release, and then press `d`. You will get the output

  ```
  [detached (from session 0)]
  ```

- Disconnect ssh as you want

  ```bash
  $ exit
  ```

- After reconnecting to ssh, attach to `tmux` session

  ```bash
  $ ssh azure
  $ tmux attach
  ```

  The program should still be running properly.

## Acknowledgement

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
- [tmux cheatsheet](https://gist.github.com/andreyvit/2921703)
- [EECS 281 ssh tips](https://piazza.com/class/ksppe8s8o73tz?cid=102)