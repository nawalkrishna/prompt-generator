# Deploying to Vercel

This guide will help you deploy your AI Prompt Generator to Vercel.

## Prerequisites

1. A [Vercel account](https://vercel.com/signup) (free tier works)
2. [Vercel CLI](https://vercel.com/cli) installed (optional but recommended)
3. Git repository pushed to GitHub, GitLab, or Bitbucket

## Deployment Methods

### Method 1: Deploy via Vercel Dashboard (Recommended for first-time)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```

2. **Import to Vercel**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New..." → "Project"
   - Import your Git repository
   - Vercel will auto-detect the configuration from `vercel.json`

3. **Configure Environment Variables** (if needed)
   - In the Vercel dashboard, go to your project settings
   - Navigate to "Environment Variables"
   - Add any custom variables if needed (optional):
     - `REACT_APP_API_URL` - Leave empty to use relative paths
     - `REACT_APP_ENABLE_HISTORY` - Set to `true`
     - `REACT_APP_ENABLE_TEMPLATES` - Set to `true`

4. **Deploy**
   - Click "Deploy"
   - Wait for the build to complete (usually 2-3 minutes)
   - Your app will be live at `https://your-project-name.vercel.app`

### Method 2: Deploy via Vercel CLI

1. **Install Vercel CLI** (if not already installed)
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy from project root**
   ```bash
   vercel
   ```

4. **Follow the prompts:**
   - Set up and deploy? **Y**
   - Which scope? Select your account
   - Link to existing project? **N** (for first deployment)
   - What's your project's name? Enter a name
   - In which directory is your code located? **.**
   - Want to override settings? **N** (vercel.json will be used)

5. **Deploy to production**
   ```bash
   vercel --prod
   ```

## Project Structure

Your project is configured as follows:

```
prompt-generator/
├── api/                    # Serverless API functions
│   └── index.py           # Main Flask API handler
├── backend/               # Backend code (imported by API)
│   ├── adapters/         # Model adapters
│   ├── app.py           # Original Flask app
│   └── ...
├── frontend/             # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
├── vercel.json          # Vercel configuration
├── requirements.txt     # Python dependencies
└── .env.production     # Production environment variables
```

## How It Works

1. **Backend as Serverless Functions**
   - The Flask backend is adapted to run as Vercel serverless functions
   - API routes are accessible at `/api/*`
   - Example: `https://your-app.vercel.app/api/generate`

2. **Frontend as Static Build**
   - React frontend is built into static files
   - Served from the root path `/`
   - API calls use relative paths to connect to serverless functions

3. **Routing**
   - `/api/*` → Serverless Python functions
   - `/*` → Static React build

## API Endpoints

Once deployed, your API will be available at:

- **Health Check**: `https://your-app.vercel.app/api/health`
- **Get Models**: `https://your-app.vercel.app/api/models`
- **Generate Prompt**: `https://your-app.vercel.app/api/generate` (POST)

## Testing Your Deployment

1. **Test the frontend**
   - Visit `https://your-app.vercel.app`
   - You should see the prompt generator interface

2. **Test the API health check**
   ```bash
   curl https://your-app.vercel.app/api/health
   ```

   Expected response:
   ```json
   {
     "status": "healthy",
     "timestamp": "2024-XX-XXTXX:XX:XX.XXXXXX"
   }
   ```

3. **Test prompt generation**
   ```bash
   curl -X POST https://your-app.vercel.app/api/generate \
     -H "Content-Type: application/json" \
     -d '{
       "modality": "text",
       "model": "gpt-4",
       "payload": {
         "goal": "Write a blog post",
         "subject": "AI in healthcare"
       }
     }'
   ```

## Troubleshooting

### Build Fails

1. **Check build logs** in Vercel dashboard
2. **Common issues:**
   - Missing dependencies in `requirements.txt`
   - Node.js version mismatch
   - Build command errors

### API Returns 500 Error

1. **Check function logs** in Vercel dashboard
2. **Common causes:**
   - Python import errors
   - Missing backend files
   - Incorrect path references

### Frontend Can't Connect to API

1. **Verify API routes** are working:
   ```bash
   curl https://your-app.vercel.app/api/health
   ```

2. **Check browser console** for CORS errors

3. **Verify frontend config**:
   - Check `frontend/src/config.js`
   - Ensure `API_BASE_URL` is using relative paths in production

### Deployment Times Out

1. **Check if frontend build is too large**
   ```bash
   cd frontend
   npm run build
   ```

2. **Optimize build size** if needed:
   - Remove unused dependencies
   - Enable tree-shaking
   - Use production build

## Custom Domain (Optional)

1. Go to your project settings in Vercel
2. Navigate to "Domains"
3. Add your custom domain
4. Follow DNS configuration instructions

## Updating Your Deployment

### Automatic Deployments

Once connected to Git, Vercel automatically deploys:
- **Production**: Commits to `main` branch
- **Preview**: Commits to other branches and PRs

### Manual Redeployment

```bash
vercel --prod
```

## Environment Variables

If you need to add environment variables:

1. **Via Dashboard**:
   - Project Settings → Environment Variables
   - Add variables
   - Redeploy

2. **Via CLI**:
   ```bash
   vercel env add VARIABLE_NAME
   ```

## Cost

- **Free Tier** includes:
  - 100 GB bandwidth per month
  - 100 GB-hours of serverless function execution
  - Unlimited static deployments

- This project should easily fit within free tier limits for moderate usage

## Support

If you encounter issues:

1. Check [Vercel Documentation](https://vercel.com/docs)
2. Review [Vercel Community](https://github.com/vercel/vercel/discussions)
3. Check this project's GitHub issues

## Next Steps

After deployment:

1. ✅ Test all functionality
2. ✅ Set up custom domain (optional)
3. ✅ Configure analytics (optional)
4. ✅ Set up monitoring
5. ✅ Share your deployed app!

---

**Your app is ready to deploy! 🚀**

Run `vercel` from the project root to get started.
