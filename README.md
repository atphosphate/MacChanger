# MacChanger

**MacChanger** is a tool designed to help users change the Media Access Control (MAC) address of their network interface cards. Changing your MAC address can enhance privacy, bypass certain network restrictions, or emulate another device on the same network.

---

## 🚨 Disclaimer
This tool is for **educational purposes only**. Unauthorized use of this tool to impersonate another device or evade network restrictions may violate legal and ethical guidelines. Use responsibly and ensure compliance with local laws.

---

## 📝 Features
- **Change MAC Address**: Spoof your MAC address to any custom value.
- **Random MAC Address**: Generate and set a random MAC address automatically.
- **Restore Original MAC Address**: Revert to the original MAC address at any time.
- **Lightweight and Easy to Use**: Simple command-line interface with minimal dependencies.

---

## 🖥️ Requirements
- Python 3.x or later
- A Linux-based operating system (tested on Ubuntu and other Debian-based distributions)
- Administrative privileges (root or sudo access)

---

## 🔧 Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/atphosphate/MacChanger.git
   cd MacChanger
   ```

2. Ensure you have the necessary permissions:
   ```bash
   sudo su
   ```

---

## 📂 File Structure
- **`macchanger.py`**: Main script for changing the MAC address.
- **`README.md`**: Documentation for the tool.

---

## ⚙️ How It Works
1. The script takes the name of the network interface as input.
2. Depending on the user's selection, it:
   - Sets a custom MAC address.
   - Generates and applies a random MAC address.
   - Restores the interface's original MAC address.
3. Uses `ifconfig` or `ip` commands to modify network interface settings.

---

## 📖 Usage
Run the script with administrative privileges to change your MAC address. 

   ```bash
   sudo python mac_changer.py -i <interface> -m <new-mac-address>
   ```

---

## 🔍 Example
```bash
$ sudo python mac_changer.py --interface eth0 --mac_address 10:10:10:10:10:10
[*] MacChanger has started
[*] Succsess!
```

---

## 🚀 Future Enhancements
- Support for non-Linux operating systems (e.g., macOS).
- A graphical user interface (GUI).
- Compatibility with network manager tools.

---

## 🧑‍💻 Contribution
Contributions are welcome! Feel free to fork this repository, submit pull requests, or open issues for feature requests and bug reports.

---

## 🛡️ Legal and Ethical Usage
This tool should only be used in authorized testing environments or with the owner's consent. Misuse for malicious purposes may lead to severe consequences.
