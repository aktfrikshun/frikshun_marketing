# Contact Form Setup Instructions

## ✅ What's Been Done

1. **Contact form integrated** - The form now uses FormSubmit (no signup required)
2. **Thank you page created** - `thank-you.html` is ready
3. **Form validation added** - Better user feedback on form submission

## 🔧 One Thing You Need to Update

In `index.html`, find this line (around line 370):
```html
<input type="hidden" name="_next" value="https://YOUR_USERNAME.github.io/frikshun_marketing/thank-you.html">
```

**Replace `YOUR_USERNAME` with your actual GitHub username.**

For example, if your GitHub username is `aktfrikshun`, change it to:
```html
<input type="hidden" name="_next" value="https://aktfrikshun.github.io/frikshun_marketing/thank-you.html">
```

## 📧 How It Works

1. User fills out the form on your site
2. Form submits to FormSubmit service
3. FormSubmit sends an email to `aktfrikshun@gmail.com`
4. User is redirected to the thank-you page

## 🧪 Testing

After updating the username:
1. Commit and push to GitHub
2. Visit your GitHub Pages site
3. Fill out the contact form
4. Submit it
5. Check your email for the submission
6. Verify you're redirected to the thank-you page

## 📝 Form Details

- **Email recipient:** aktfrikshun@gmail.com
- **Subject line:** "New Contact from FrikShun Website"
- **Fields:** Name, Email, Company (optional), Project Details
- **Spam protection:** Enabled via FormSubmit

## 🎨 Customization Options

If you want to customize further, you can:
- Change the subject line by editing the `_subject` hidden input
- Modify the thank-you page message
- Add more form fields if needed

The form is ready to use once you update the GitHub username!

