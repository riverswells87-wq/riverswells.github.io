---
title: "Contact"
permalink: /contact/
---

I would love to hear from you. Whether you have a job opportunity, want to collaborate, or just want to connect, fill out the form below and I will get back to you as soon as possible.

<style>
.contact-form input,
.contact-form select,
.contact-form textarea {
  width: 100%;
  padding: 0.6em;
  margin-bottom: 0.75em;
  border: 1px solid #d3d3d3;
  border-radius: 3px;
  font-size: 0.95em;
  font-family: inherit;
  box-sizing: border-box;
}
.contact-form textarea { height: 150px; resize: vertical; }
.contact-form button {
  padding: 0.6em 2em;
  background: #1A2B3C;
  color: #fff;
  border: none;
  border-radius: 3px;
  font-size: 0.95em;
  cursor: pointer;
}
.contact-form button:hover { background: #2E5E8E; }
.success-message {
  display: none;
  background: #d4edda;
  color: #155724;
  padding: 0.75em;
  border-radius: 3px;
  margin-top: 1em;
}
</style>

<div class="contact-form">
  <form id="contact-form" action="https://formspree.io/f/xwvyjvnw" method="POST">
    <input type="text" name="name" placeholder="Your Name" required />
    <input type="email" name="email" placeholder="Your Email" required />
    <select name="subject" required>
      <option value="" disabled selected>Subject</option>
      <option value="Job Opportunity">Job Opportunity</option>
      <option value="Collaboration">Collaboration</option>
      <option value="Speaking or Writing">Speaking or Writing</option>
      <option value="Other">Other</option>
    </select>
    <textarea name="message" placeholder="Your message..." required></textarea>
    <button type="submit">Send Message</button>
  </form>
  <div class="success-message" id="success-msg">
    Thanks for reaching out. I will be in touch soon.
  </div>
</div>

<script>
  var form = document.getElementById('contact-form');
  var success = document.getElementById('success-msg');
  if (form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { 'Accept': 'application/json' }
      }).then(function(r) {
        if (r.ok) {
          form.reset();
          form.style.display = 'none';
          success.style.display = 'block';
        }
      });
    });
  }
</script>
