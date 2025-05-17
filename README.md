---

# Auto\_Tor\_IP\_Changer v2.1 🚀

Automatically change your IP address using the power of the TOR network.
Perfect for privacy enthusiasts, security researchers, and anyone who wants to automate IP rotation.

---

## 🧰 Features

* Auto IP change using the TOR network
* Set change intervals (in seconds)
* Infinite or limited IP changes
* Installs dependencies automatically (TOR, `requests[socks]`)
* Use anywhere with the simple `aut` command

---

## ⚙️ Requirements

> These will be auto-installed if missing.

```bash
sudo apt-get install tor
pip3 install requests[socks]
```

---

## 🧑‍💻 Installation Steps

```bash
git clone https://github.com/FDX100/Auto_Tor_IP_changer.git
cd Auto_Tor_IP_changer
python3 install.py
```

> 🎉 After installation, just type `aut` from anywhere in the terminal!

---

## 🚀 Usage Guide

1. Run the tool:

   ```bash
   aut
   ```

2. Enter the **time interval in seconds** between IP changes (e.g. `60` for 1 min).

3. Enter how many times you want to change your IP:

   * Enter `0` for **infinite** IP changes.

4. Configure your browser or PC SOCKS proxy settings to:

   ```
   127.0.0.1:9050
   ```

5. Enjoy anonymous browsing with rotating IPs!

---

## 📢 Notes

* Make sure TOR is allowed through your firewall.
* This tool only works if TOR is functioning correctly on your system.
* Always use this ethically and legally.

---

## 🤖 Developer

Made with ❤️ by **mrFD**
[🔗 Facebook Page](http://facebook.com/ninja.hackerz.kurdish/)

---


