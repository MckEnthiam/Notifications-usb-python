#include <stdio.h>
#include <string.h>
#include <process.h>

int main(int argc, char *argv[]) {
    if (argc < 3) {
        fprintf(stderr, "Usage: notif_usb.exe <titre> <message>\n");
        return 1;
    }

    char *cmd[] = {
        "adb", "shell", "cmd", "notification", "post",
        "-S", "bigtext",
        "-t", argv[1],
        "python_notif",
        argv[2],
        NULL
    };

    _spawnvp(_P_WAIT, "adb", (const char * const *)cmd);

    return 0;
}
