# 🔑 Google Gemini API Setup Guide

## Step 1: Get Your Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click **"Create API Key"**
4. Copy your API key (it will look like: `AIzaSy...`)

## Step 2: Set Environment Variable

### Option A: Set in Terminal (Temporary - for current session)
```bash
export GEMINI_API_KEY="your-api-key-here"
```

### Option B: Add to your shell profile (Permanent)
Add this line to your `~/.zshrc` or `~/.bash_profile`:
```bash
export GEMINI_API_KEY="your-api-key-here"
```

Then reload:
```bash
source ~/.zshrc  # or source ~/.bash_profile
```

### Option C: Create a `.env` file (Recommended for development)
Create a `.env` file in your project directory:
```
GEMINI_API_KEY=your-api-key-here
```

Then install python-dotenv and load it in your app:
```bash
pip install python-dotenv
```

## Step 3: Verify Setup

Test that the API key is set:
```bash
echo $GEMINI_API_KEY
```

## Step 4: Install Dependencies

```bash
cd "/Users/ananyamangal/DLI-chatbot/Desktop/DLI project/ananya new"
pip install -r requirements.txt
```

## 🎯 Quick Start

1. Set your API key: `export GEMINI_API_KEY="your-key"`
2. Start Flask: `python app.py`
3. Start ngrok: `ngrok http 5002`
4. Configure Twilio webhook with ngrok URL
5. Test by sending an image to your WhatsApp sandbox!

---

**Note:** Keep your API key secure! Never commit it to version control.









# 🚀 How to Start Ngrok

## Quick Start

**In a NEW terminal window:**

```bash
ngrok http 5002
```

That's it! 🎉

---

## Detailed Steps

### 1. Open a New Terminal
- Don't use the same terminal where Flask is running
- Open a completely new terminal window/tab

### 2. Navigate to Your Project (Optional)
```bash
cd "/Users/ananyamangal/DLI-chatbot/Desktop/DLI project/ananya new"
```

### 3. Start Ngrok
```bash
ngrok http 5002
```

**Note:** The port `5002` must match the port your Flask app is running on (check `app.py` - it should be `port=5002`)

### 4. Copy the HTTPS URL
You'll see output like:
```
Forwarding    https://abc123xyz.ngrok-free.app -> http://localhost:5002
```

Copy the `https://` URL (e.g., `https://abc123xyz.ngrok-free.app`)

### 5. Update Twilio Webhook
1. Go to [Twilio Console](https://console.twilio.com/us1/develop/sms/sandbox)
2. Paste your ngrok URL + `/whatsapp`:
   ```
   https://abc123xyz.ngrok-free.app/whatsapp
   ```
3. Save

---

## Keep Both Terminals Running

- **Terminal 1:** Flask app (`python app.py`)
- **Terminal 2:** Ngrok (`ngrok http 5002`)

Both must stay running for the bot to work!

---

## Troubleshooting

### "Command not found: ngrok"
Install ngrok first:
```bash
brew install ngrok/ngrok/ngrok
```

Or download from: https://ngrok.com/download

### "Port 5002 is already in use"
Either:
- Stop whatever is using port 5002, OR
- Change Flask to use a different port and update ngrok command

### Ngrok URL changes every time
- Free ngrok URLs change on restart
- You'll need to update Twilio webhook URL each time
- For production, use ngrok paid plan for fixed URLs

---

## View Ngrok Web Interface

While ngrok is running, open:
```
http://127.0.0.1:4040
```

This shows all requests going through ngrok - useful for debugging!




# 🚀 Complete Setup Guide: Flask + Twilio Sandbox + Ngrok Integration

## Prerequisites
- Python 3.x installed
- Flask and Twilio installed (`pip install -r requirements.txt`)
- Twilio account (free tier works)
- Ngrok account (free tier works)

---

## Step 1: Install Ngrok

### macOS (using Homebrew):
```bash
brew install ngrok/ngrok/ngrok
```

### Or download directly:
1. Go to https://ngrok.com/download
2. Download for macOS
3. Unzip and move to `/usr/local/bin/` or add to your PATH
4. Sign up for a free account at https://dashboard.ngrok.com/signup
5. Get your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
6. Authenticate: `ngrok config add-authtoken YOUR_AUTHTOKEN`

---

## Step 2: Start Your Flask Application

**In Terminal 1:**
```bash
cd "/Users/ananyamangal/DLI-chatbot/Desktop/DLI project/ananya new"
python app.py
```

You should see:
```
 * Running on http://0.0.0.0:5002
 * Debug mode: on
```

**Keep this terminal running!**

---

## Step 3: Start Ngrok in a NEW Terminal

**In Terminal 2 (NEW TERMINAL):**
```bash
ngrok http 5002
```

You'll see output like:
```
ngrok                                                                              
                                                                                   
Session Status                online                                              
Account                       Your Name (Plan: Free)                              
Version                       3.x.x                                               
Region                        United States (us)                                  
Latency                       -                                                    
Web Interface                 http://127.0.0.1:4040                               
Forwarding                    https://abc123xyz.ngrok-free.app -> http://localhost:5002
                                                                                   
Connections                   ttl     opn     rt1     rt5     p50     p90         
                              0       0       0.00    0.00    0.00    0.00        
```

**Important:** Copy the `https://` URL (e.g., `https://abc123xyz.ngrok-free.app`)

**Keep this terminal running too!**

---

## Step 4: Configure Twilio WhatsApp Sandbox

### 4.1 Access Twilio Console
1. Go to https://console.twilio.com/
2. Navigate to **Messaging** → **Try it out** → **Send a WhatsApp message**
3. Or go directly to: https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn

### 4.2 Join the Sandbox
1. You'll see a sandbox number (e.g., `+1 415 555 1234`)
2. Send the join code to that number from your WhatsApp
3. Example: If the code is `join example-code`, send exactly that message

### 4.3 Configure Webhook URL
1. In Twilio Console, go to **Messaging** → **Settings** → **WhatsApp Sandbox Settings**
2. Or navigate to: https://console.twilio.com/us1/develop/sms/sandbox
3. Find the **"When a message comes in"** field
4. Enter your ngrok URL + `/whatsapp` endpoint:
   ```
   https://abc123xyz.ngrok-free.app/whatsapp
   ```
   (Replace `abc123xyz.ngrok-free.app` with YOUR actual ngrok URL)
5. Set HTTP method to **POST**
6. Click **Save**

---

## Step 5: Test the Integration

1. **Send a WhatsApp message** to your Twilio sandbox number
2. **Check Terminal 1** (Flask) - you should see debug logs
3. **Check Terminal 2** (ngrok) - you should see HTTP requests in the web interface at http://127.0.0.1:4040
4. **Check Twilio Console** → **Monitor** → **Logs** → **Messaging** to see webhook calls

---

## 🔧 Troubleshooting

### Issue: Ngrok URL changes every time
**Solution:** 
- Free ngrok URLs change on restart
- For production, use ngrok paid plan or deploy to a server
- Or use ngrok config file to set a custom domain (paid feature)

### Issue: "Webhook validation failed" in Twilio
**Solution:**
- Make sure your Flask app is running
- Make sure ngrok is running
- Verify the webhook URL ends with `/whatsapp`
- Check that the URL uses `https://` (not `http://`)

### Issue: "Connection refused" in ngrok
**Solution:**
- Make sure Flask app is running on port 5002
- Check: `lsof -i :5002` to see if something is using the port
- Try: `python app.py` again

### Issue: Messages not being received
**Solution:**
- Verify you've joined the sandbox correctly
- Check Twilio Console → Logs for errors
- Check Flask terminal for error messages
- Verify webhook URL in Twilio matches your ngrok URL

---

## 📝 Quick Reference Commands

### Terminal 1 - Flask App:
```bash
cd "/Users/ananyamangal/DLI-chatbot/Desktop/DLI project/ananya new"
python app.py
```

### Terminal 2 - Ngrok:
```bash
ngrok http 5002
```

### Check if Flask is running:
```bash
curl http://localhost:5002/whatsapp
```

### View ngrok web interface:
Open browser to: http://127.0.0.1:4040

---

## 🎯 Complete Flow Diagram

```
WhatsApp Message
    ↓
Twilio Sandbox
    ↓
Ngrok Tunnel (https://xxx.ngrok-free.app)
    ↓
Your Local Flask App (localhost:5002)
    ↓
/webhook endpoint processes message
    ↓
Response sent back through same path
    ↓
WhatsApp User receives reply
```

---

## ⚠️ Important Notes

1. **Ngrok free tier limitations:**
   - URL changes on restart
   - Session timeout after 2 hours of inactivity
   - Limited requests per minute

2. **For development:**
   - Keep both terminals open
   - Restart ngrok if you see connection errors
   - Update Twilio webhook URL if ngrok URL changes

3. **For production:**
   - Deploy Flask app to a server (Heroku, AWS, etc.)
   - Use a fixed domain name
   - Set up proper SSL certificates

---

## 🎉 You're All Set!

Once everything is running:
- Flask app: ✅ Running on port 5002
- Ngrok: ✅ Tunneling to your Flask app
- Twilio: ✅ Webhook configured
- WhatsApp: ✅ Ready to receive messages!

Send a test message to your sandbox number and watch the magic happen! 🚀




# 🔑 Twilio Credentials Setup

## Why You Need Twilio Credentials

When users send images through WhatsApp via Twilio, the media URLs require authentication to download. You need to add your Twilio Account SID and Auth Token.

## How to Get Your Twilio Credentials

1. Go to [Twilio Console](https://console.twilio.com/)
2. Log in to your account
3. Your **Account SID** and **Auth Token** are displayed on the dashboard homepage
4. Or go to: https://console.twilio.com/us1/account/settings/credentials

## Add to .env File

Add these lines to your `.env` file:

```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
```

**Example:**
```
GEMINI_API_KEY=AIzaSyB2XLcnFZ0xvIKX7GBqxr6PeoOPgQu9uA0
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your_auth_token_here
```

## Security Note

⚠️ **Never commit your `.env` file to version control!** It contains sensitive credentials.

The `.env` file is already in `.gitignore` to protect your credentials.

---

After adding the credentials, restart your Flask app for the changes to take effect.











