import flet as ft
import subprocess
import json

def main(page: ft.Page):
    page.title = "NSS Cyber-Sentinel HUD"
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.START

    output_box = ft.TextField(
        label="Tactical Event Feed",
        multiline=True,
        read_only=True,
        min_lines=10,
        max_lines=14,
        border_color=ft.colors.CYAN_400,
        text_style=ft.TextStyle(font_family="monospace", size=12),
    )

    def run_audit(e):
        output_box.value = "[*] Executing unprivileged field telemetry audit...\n"
        page.update()
        try:
            addr_res = subprocess.run(["ip", "addr"], capture_output=True, text=True, timeout=3)
            telemetry = ["📡 Active Interface Bindings:"]
            if addr_res.returncode == 0:
                for line in addr_res.stdout.splitlines():
                    if "inet " in line or "wlan0" in line:
                        telemetry.append(f"  {line.strip()}")
            
            wifi_res = subprocess.run(["termux-wifi-scaninfo"], capture_output=True, text=True, timeout=5)
            if wifi_res.returncode == 0 and wifi_res.stdout.strip():
                nets = json.loads(wifi_res.stdout)
                telemetry.append(f"\n🔍 Discovered Access Points: {len(nets)}")
                for net in nets[:3]:
                    ssid = net.get("ssid") or "[HIDDEN]"
                    rssi = net.get("rssi", "N/A")
                    telemetry.append(f"  • {ssid} ({rssi} dBm)")
            
            output_box.value = "\n".join(telemetry)
        except Exception as ex:
            output_box.value = f"[-] Audit exception: {ex}"
        page.update()

    def run_port_scan(e):
        target = target_input.value.strip()
        if not target:
            output_box.value = "[-] Error: Please enter a target IP address."
            page.update()
            return
        
        output_box.value = f"[*] Initiating TCP connect scan on {target}...\n"
        page.update()
        try:
            res = subprocess.run(["nmap", "-sT", "--top-ports", "15", target], capture_output=True, text=True, timeout=15)
            if res.returncode == 0:
                scan_results = [f"[+] Scan Results for {target}:"]
                for line in res.stdout.splitlines():
                    if "open" in line or "closed" in line or "filtered" in line:
                        scan_results.append(f"  {line.strip()}")
                output_box.value = "\n".join(scan_results)
            else:
                output_box.value = f"[-] Nmap error: {res.stderr.strip()}"
        except Exception as ex:
            output_box.value = f"[-] Scan exception: {ex}"
        page.update()

    target_input = ft.TextField(
        label="Target IP / Gateway",
        value="192.168.1.1",
        border_color=ft.colors.BLUE_GREY_400,
    )

    page.add(
        ft.Text("🛡️ NSS CYBER-SENTINEL FIELD NODE", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN_ACCENT),
        ft.Divider(),
        target_input,
        ft.Row([
            ft.ElevatedButton("Run Telemetry Audit", icon=ft.icons.RADAR, on_click=run_audit, bgcolor=ft.colors.BLUE_900),
            ft.ElevatedButton("TCP Port Scan", icon=ft.icons.SECURITY, on_click=run_port_scan, bgcolor=ft.colors.RED_900),
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        ft.VerticalDivider(height=10),
        output_box,
    )

if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
