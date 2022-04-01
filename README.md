# UMich ULCS Course Monitor

## About

With the [Two Course Limit](https://cse.engin.umich.edu/academics/for-current-students/advising/enrollment/) rules for UMich EECS Upper Level courses, if you want to enroll in more than two ULCS, you had better pay attention to whether the third course has its waitlist open so that you can get in the list early enough. This script is designed to monitor the open seats in the ULCS course you want to enroll in. As soon as the available seats become 0, it will send a notifying email.

## Getting Started

- Install `bs4`
    ```bash
    pip3 install bs4
    ```

- Configure `SENDER_EMAIL`, `SENDER_PASSWORD`, `RECEIVER_EMAIL`, and `INTERVAL`.

- Add the courses you want to monitor in `main()`. For example, EECS 482:

    ```python
    Monitor(482)
    ```

- Run the script

    ```bash
    python3 monitor.py
    ```

- To exit, press `Ctrl+C`

    - If the process failed to exit properly, refer to [this link](https://superuser.com/questions/446808/how-to-manually-stop-a-python-script-that-runs-continuously-on-linux).

## Acknowledgement

- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)