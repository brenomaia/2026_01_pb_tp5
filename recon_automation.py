import subprocess
import nmap
import json
from pathlib import Path

class ReconAutomation:
    def __init__(self, target, wordlist):
        self.target = target
        self.wordlist = wordlist

        self.results = {
            "target": target,
            "dns": {},
            "hosts": {}
        }

    def run_dnsrecon(self):
        cmd = [
            "dnsrecon",
            "-d", self.target,
            "-t", "std"
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        self.results["dns"]["raw_output"] = result.stdout
        print("Terminou subprocess recon")

    def run_subdomain_bruteforce(self):
        cmd = [
            "dnsrecon",
            "-d", self.target,
            "-D", self.wordlist,
            "-t", "brt"
        ]

        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )

        self.results["dns"]["bruteforce_output"] = result.stdout

    def scan_host(self, host):
        scanner = nmap.PortScanner()

        scanner.scan(
            hosts=host,
            arguments="-F -sV --script discovery,safe"
        )

        self.results["hosts"][host] = scanner._scan_result

    def save_report(self):
        with open("relatorio_recon.json", "w") as f:
            json.dump(
                self.results,
                f,
                indent=4
            )

    def print_summary(self):
        print("=" * 50)
        print("RELATÓRIO AUTOMATIZADO")
        print("=" * 50)
        print(f"Alvo: {self.target}")
        print(f"Hosts analisados: {len(self.results['hosts'])}")

if __name__ == "__main__":
    recon = ReconAutomation(
        target="example.com",
        wordlist="subdomains-top10.txt"
    )

    recon.run_dnsrecon()
    recon.run_subdomain_bruteforce()

    hosts = [
        "scanme.nmap.org",
        "zonetransfer.me"
    ]

    for host in hosts:
        recon.scan_host(host)

    recon.save_report()
    recon.print_summary()