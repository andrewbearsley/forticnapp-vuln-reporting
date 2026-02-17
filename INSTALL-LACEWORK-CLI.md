# Installing and configuring Lacework CLI

## Installation

### macOS

**Option 1 - Homebrew:**
```bash
brew install lacework/tap/lacework-cli
```

**Option 2 - Bash script:**
```bash
curl https://raw.githubusercontent.com/lacework/go-sdk/main/cli/install.sh | bash
```

### Windows

**Option 1 - PowerShell script:**
1. Open PowerShell as Administrator
2. Run:
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/lacework/go-sdk/main/cli/install.ps1'))
```
3. The CLI is installed at `C:\ProgramData\Lacework\lacework.exe` and PATH is updated
4. Open a new PowerShell terminal to use the CLI

**Option 2 - Chocolatey:**
```powershell
choco install lacework-cli
```

### Verify installation

```bash
lacework version
```

## Get a Lacework API key

Before configuring the CLI, you need to create an API key:

1. Log in to your FortiCNAPP account:
   - **Via FortiCloud**: Go to Services > Show More > Lacework FortiCNAPP
   - **Direct login**: `https://<your-account>.lacework.net`
2. Navigate to Settings > API Keys
3. Click "Create New" to generate a new API key
4. Copy the following values:
   - Account name (e.g., `your-account`)
   - Key ID
   - Secret key (shown only once, save it securely)

Create a JSON file with these credentials:

```json
{
  "account": "your-account",
  "keyId": "your-key-id",
  "secret": "your-secret-key"
}
```

Save this file securely (e.g., `api-key/mykey.json`).

## Configuration

Configure the CLI using the JSON file:

```bash
lacework configure -j /path/to/your-credentials.json
```

### Verify configuration

```bash
lacework configure list
```

## Reference

- <a href="https://docs.fortinet.com/document/forticnapp/latest/cli-reference" target="_blank">Lacework CLI documentation</a>
