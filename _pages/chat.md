---
title: "Chat with My Portfolio"
layout: splash
permalink: /chat/
---

<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600&display=swap');

  .page__hero, .page__title { display: none; }

  .chat-wrapper {
    font-family: 'DM Sans', sans-serif;
    max-width: 700px;
    margin: 40px auto;
    padding: 0 16px;
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .chat-header {
    display: flex;
    align-items: center;
    gap: 14px;
  }

  .avatar {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    background: linear-gradient(135deg, #7c6ff7, #a78bfa);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 22px;
    flex-shrink: 0;
  }

  .header-text h2 {
    font-size: 18px;
    font-weight: 600;
    margin: 0;
    color: #1a1a2e;
  }

  .header-text p {
    font-size: 13px;
    color: #666;
    margin: 3px 0 0;
  }

  .status-dot {
    display: inline-block;
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: #4ade80;
    margin-right: 5px;
  }

  .chat-window {
    background: #f8f8fc;
    border: 1px solid #e2e0f5;
    border-radius: 16px;
    height: 460px;
    overflow-y: auto;
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 18px;
    scroll-behavior: smooth;
  }

  .chat-window::-webkit-scrollbar { width: 4px; }
  .chat-window::-webkit-scrollbar-thumb { background: #ddd; border-radius: 4px; }

  .message { display: flex; gap: 10px; animation: fadeUp 0.2s ease; }
  .message.user { flex-direction: row-reverse; }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(6px); }
    to   { opacity: 1; transform: translateY(0); }
  }

  .msg-icon {
    width: 30px; height: 30px;
    border-radius: 50%;
    flex-shrink: 0;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px;
    margin-top: 2px;
  }
  .msg-icon.ai   { background: rgba(124,111,247,0.12); color: #7c6ff7; }
  .msg-icon.user { background: #7c6ff7; color: #fff; }

  .bubble {
    max-width: 82%;
    padding: 12px 16px;
    border-radius: 14px;
    font-size: 14.5px;
    line-height: 1.6;
  }

  .message.ai .bubble {
    background: #fff;
    border: 1px solid #e2e0f5;
    border-top-left-radius: 4px;
    color: #222;
  }

  .message.user .bubble {
    background: #7c6ff7;
    border-top-right-radius: 4px;
    color: #fff;
  }

  .suggestions {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 12px;
  }

  .suggestion-chip {
    background: rgba(124,111,247,0.08);
    border: 1px solid rgba(124,111,247,0.25);
    color: #7c6ff7;
    font-size: 12.5px;
    padding: 6px 12px;
    border-radius: 20px;
    cursor: pointer;
    font-family: 'DM Sans', sans-serif;
    transition: background 0.15s;
  }
  .suggestion-chip:hover { background: rgba(124,111,247,0.15); }

  .typing-indicator {
    display: flex; align-items: center; gap: 5px;
    padding: 12px 16px;
    background: #fff;
    border: 1px solid #e2e0f5;
    border-radius: 14px;
    border-top-left-radius: 4px;
    width: fit-content;
  }

  .dot {
    width: 7px; height: 7px;
    background: #aaa; border-radius: 50%;
    animation: bounce 1.2s infinite;
  }
  .dot:nth-child(2) { animation-delay: 0.2s; }
  .dot:nth-child(3) { animation-delay: 0.4s; }

  @keyframes bounce {
    0%, 60%, 100% { transform: translateY(0); }
    30%            { transform: translateY(-5px); }
  }

  .chat-input-area {
    display: flex;
    gap: 10px;
    align-items: flex-end;
  }

  #user-input {
    flex: 1;
    background: #f8f8fc;
    border: 1px solid #e2e0f5;
    border-radius: 12px;
    color: #222;
    font-family: 'DM Sans', sans-serif;
    font-size: 14px;
    padding: 13px 16px;
    resize: none;
    outline: none;
    line-height: 1.5;
    min-height: 48px;
    max-height: 140px;
    transition: border-color 0.15s;
  }
  #user-input::placeholder { color: #aaa; }
  #user-input:focus { border-color: #7c6ff7; }

  #send-btn {
    background: #7c6ff7;
    border: none;
    border-radius: 12px;
    color: #fff;
    cursor: pointer;
    width: 48px; height: 48px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
    transition: opacity 0.15s, transform 0.1s;
  }
  #send-btn:hover   { opacity: 0.88; transform: scale(1.04); }
  #send-btn:disabled { opacity: 0.4; cursor: not-allowed; transform: none; }

  .powered-by {
    text-align: center;
    font-size: 11.5px;
    color: #aaa;
    letter-spacing: 0.3px;
  }
</style>

<div class="chat-wrapper">
  <div class="chat-header">
    <div class="avatar">👩‍💻</div>
    <div class="header-text">
      <h2>Ask About Marion's Work</h2>
      <p><span class="status-dot"></span>AI-powered · Knows Marion's full background</p>
    </div>
  </div>

  <div class="chat-window" id="chat-window">
    <div class="message ai">
      <div class="msg-icon ai">✦</div>
      <div>
        <div class="bubble">
          Hey there! 👋 I'm here to answer any questions about Marion's professional background — her experience, skills, projects, and more. What would you like to know?
        </div>
        <div class="suggestions">
          <button class="suggestion-chip" onclick="sendSuggestion(this)">What industries has she worked in?</button>
          <button class="suggestion-chip" onclick="sendSuggestion(this)">What are her top skills?</button>
          <button class="suggestion-chip" onclick="sendSuggestion(this)">Tell me about her most recent role</button>
          <button class="suggestion-chip" onclick="sendSuggestion(this)">What AI projects has she built?</button>
        </div>
      </div>
    </div>
  </div>

  <div class="chat-input-area">
    <textarea id="user-input" placeholder="Ask anything about Marion's experience…" rows="1"></textarea>
    <button id="send-btn" onclick="sendMessage()">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
        <line x1="22" y1="2" x2="11" y2="13"></line>
        <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
      </svg>
    </button>
  </div>

  <div class="powered-by">powered by Claude · built for Marion's portfolio</div>
</div>

<script>
const RESUME_CONTEXT = `
Rivers Wells — Resume

CONTACT
Everett, WA | 205.522.6027 | riverswells87@gmail.com | linkedin.com/in/marion-rivers-wells | riverswells.com

TITLE: Senior Program/Content Manager
Specialties: Content Strategy | Technical Writing | LLM Development | UX/CX Design | Data Research & Validation

SUMMARY
Program Manager and Content Strategist specializing in AI-driven data accessibility, data research and validation, and documentation infrastructure at scale. With 9+ years at Amazon, built AI tooling that delivers BI insights in under 2 minutes, conducted multi-week data quality investigations that reshaped how leadership understands operational metrics, and owned content programs reaching millions of readers and recipients.

CORE COMPETENCIES
- Program & Project Management: End-to-end project ownership, stakeholder management, cross-functional coordination, Workfront, data-driven reporting.
- Content Strategy & Management: CMS platforms, content audits, information architecture, localization (ATMS), accessibility (WCAG).
- Communications: Enterprise-scale internal comms, campaign planning, multi-group approval workflows, audience segmentation.
- Technical Writing: SOPs, wiki documentation, style guides, UX writing, video scripting & production.
- Data & Metrics: Efficacy analysis, KPI reporting, Excel (WoW/T4W/MoM/YTD automation), deep-dive narratives.
- Tools & Platforms: Workfront, Slack, PowerShell, Microsoft Office Suite, ATMS, Adobe Creative Cloud.

SKILLS
Program & Project Management | AI Tooling & Automation | Data Research & Validation | BI Accessibility | Content Strategy | Enterprise Communications | Stakeholder Management | UX Research | LLM Interface Design | Technical Writing | CMS Platforms | UX/CX Development | SQL | QuickSight | PowerShell | Excel | Adobe Creative Cloud

EXPERIENCE

Amazon, Inc. — Seattle, WA | January 2023 – Present
Program Manager, ICON Data & Documentation
- Owned the program roadmap for AI-driven data accessibility and documentation infrastructure across a VP-level organization within Amazon's Intelligent Cloud Hosting (ICON) group.
- Designed, developed, and soft-launched the ICON Data Assistant, an LLM-powered AI agent enabling natural language queries across operational BI data for operations management (March 2026). Delivers insights and reports in under 2 minutes. Presented at the 2026 internal Hackathon.
- Developed AI-driven tooling proposals cutting PMO document creation time by 80%. Designed a scalable LLM-guided experience for internal communication standards.
- Conducted a 3-week data quality audit across BI formats, producing 3 reports with SQL validation queries and case studies. Findings restructured ticket management.
- Established dashboard creation best practices; resolved a QuickSight sharing blocker reducing dashboard dev time from 1-2 weeks to ~5 minutes.

Amazon, Inc. — Seattle, WA | January 2022 – January 2023
Project Manager, IT Support Site
- Sole program owner of it.amazon.com, Amazon's global internal IT support site (~350,000 monthly readers).
- Designed a single-operator intake model resolving 335+ content requests in 7 months at >100% resolution rate.
- Directed two CMS migrations, completing 676 articles two weeks ahead of schedule.
- Trained 30+ team members on the new CMS. Volunteered as content quality Bar Raiser.

Amazon, Inc. — Seattle, WA | June 2021 – January 2022
Communications Program Manager
- Owned end-to-end enterprise communications campaigns reaching ~1.7 million Amazon employees.
- Drove Office 2016-to-2019 upgrade campaign for 330k employees; 97.96% upgraded in 60 days.
- Exceeded Amazon Chime 5 adoption goal by 283% (198,562 vs. 70k target). Achieved 89.89% macOS security compliance in 22 days.

Amazon, Inc. — Seattle, WA | April 2018 – June 2021
Technical Writer / Program Manager
- Wrote and managed technical documentation for it.amazon.com (global IT support site).
- Created the global IT content intake model; managed 5,357 submissions and resolved 1,256 (23.45%).
- Produced educational video tutorials accumulating 1.5MM+ views with 55% average engagement rate.
- Built Excel automation for WoW, T4W, MoM, and YTD metric calculations.
- Built virtual onboarding experience (42 articles) supporting 57,750 FTEs, 7,400 contractors, and 10,187 interns globally.

Amazon, Inc. — Seattle, WA | October 2016 – April 2018
IT Support Engineer
- Provided deskside IT support in Seattle.
- Completed ~6,000 tickets with 100% customer satisfaction rating.
- Selected for a 3-month rotation with Global IT Content Management; converted to Technical Writer role.

EDUCATION
Bachelor of Science, Marketing — Auburn University
CompTIA A+ Certification
`;

// Replace this with your Netlify function URL after deploying
const PROXY_URL = 'https://YOUR-NETLIFY-SITE.netlify.app/.netlify/functions/claude-proxy';

const conversationHistory = [];

async function callClaude(userMessage) {
  conversationHistory.push({ role: "user", content: userMessage });

  const systemPrompt = `You are a friendly, conversational assistant embedded on Marion Rivers Wells's portfolio website. Your ONLY job is to answer questions about Marion's professional background, skills, experience, and education based on her resume below.

If someone asks about something not covered in the resume, kindly let them know you can only speak to her professional background, and suggest a related question you CAN answer.

Keep answers warm, concise, and natural — like a knowledgeable colleague talking about Marion, not a robot reciting a resume. Use first name "Marion" naturally. Don't bullet-point everything; mix in prose. Be enthusiastic about her accomplishments.

MARION'S RESUME:
${RESUME_CONTEXT}`;

  const response = await fetch(PROXY_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      system: systemPrompt,
      messages: conversationHistory
    })
  });

  if (!response.ok) throw new Error('Proxy error');
  const data = await response.json();
  const reply = data.content?.[0]?.text || "Sorry, I had trouble with that. Try asking something else!";
  conversationHistory.push({ role: "assistant", content: reply });
  return reply;
}

function appendMessage(role, text) {
  const win = document.getElementById('chat-window');
  const div = document.createElement('div');
  div.className = `message ${role}`;
  div.innerHTML = `
    <div class="msg-icon ${role}">${role === 'ai' ? '✦' : '→'}</div>
    <div class="bubble">${text.replace(/\n/g, '<br>')}</div>
  `;
  win.appendChild(div);
  win.scrollTop = win.scrollHeight;
}

function showTyping() {
  const win = document.getElementById('chat-window');
  const div = document.createElement('div');
  div.className = 'message ai'; div.id = 'typing';
  div.innerHTML = `<div class="msg-icon ai">✦</div><div class="typing-indicator"><div class="dot"></div><div class="dot"></div><div class="dot"></div></div>`;
  win.appendChild(div);
  win.scrollTop = win.scrollHeight;
}

function removeTyping() { document.getElementById('typing')?.remove(); }

async function sendMessage() {
  const input = document.getElementById('user-input');
  const btn = document.getElementById('send-btn');
  const text = input.value.trim();
  if (!text) return;
  input.value = ''; input.style.height = 'auto'; btn.disabled = true;
  appendMessage('user', text);
  showTyping();
  try {
    const reply = await callClaude(text);
    removeTyping();
    appendMessage('ai', reply);
  } catch(e) {
    removeTyping();
    appendMessage('ai', "Hmm, something went wrong. Give it another shot!");
  }
  btn.disabled = false;
  input.focus();
}

function sendSuggestion(btn) {
  document.getElementById('user-input').value = btn.textContent;
  sendMessage();
}

document.getElementById('user-input').addEventListener('input', function() {
  this.style.height = 'auto';
  this.style.height = Math.min(this.scrollHeight, 140) + 'px';
});

document.getElementById('user-input').addEventListener('keydown', function(e) {
  if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); sendMessage(); }
});
</script>
