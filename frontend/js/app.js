const API = window.location.origin.includes('localhost') ? 'http://localhost:8000' : window.location.origin;
let jobId = null, poll = null, data = {};

// Fill example
function fill(btn) {
    document.getElementById('idea').value = 'Create a startup that offers ' + btn.textContent;
    document.getElementById('idea').focus();
}

// Launch
async function launch() {
    const idea = document.getElementById('idea').value.trim();
    if (!idea) { toast('Type your startup idea first', 'err'); return; }

    const btn = document.getElementById('go');
    btn.disabled = true; btn.textContent = '⏳ Launching...';

    try {
        await fetch(API + '/api/history', { signal: AbortSignal.timeout(3000) });
        const r = await fetch(API + '/api/run', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ startup_idea: idea })
        });
        const d = await r.json();
        jobId = d.job_id;
        toast('Agents started! Job: ' + jobId, 'ok');
        showProgress();
        startPoll();
    } catch (e) {
        toast('Cannot reach API. Run: uvicorn api:app --port 8000', 'err');
        btn.disabled = false; btn.textContent = '🚀 Launch Company';
    }
}

// Polling
function startPoll() {
    let step = 0;
    const timers = [0, 2000, 20000, 40000, 60000, 80000];
    timers.forEach((t, i) => {
        setTimeout(() => { if (i < 5) setStep(i, Math.min(15 + i * 18, 90)); }, t);
    });

    poll = setInterval(async () => {
        try {
            const r = await fetch(API + '/api/status/' + jobId);
            const s = await r.json();
            if (s.status === 'completed') { clearInterval(poll); await getResults(); }
            if (s.status === 'failed') { clearInterval(poll); toast('Failed: ' + (s.error || '?'), 'err'); resetBtn(); }
        } catch (e) {}
    }, 2500);
}

async function getResults() {
    const r = await fetch(API + '/api/results/' + jobId);
    const d = await r.json();
    if (d.results) { data = d.results; render(data); }
}

// Progress UI
function showProgress() {
    document.getElementById('input-card').style.display = 'none';
    document.getElementById('progress').classList.add('show');
    document.getElementById('results-section').classList.remove('show');
    setDots('idle');
}

function setStep(i, pct) {
    document.getElementById('bar').style.width = pct + '%';
    document.getElementById('pct').textContent = pct + '%';
    const names = ['ceo', 'research', 'dev', 'mkt', 'support'];
    for (let j = 0; j < 5; j++) {
        const el = document.getElementById('s' + j);
        const num = el.querySelector('.step-num');
        if (j < i) { el.className = 'step done'; num.textContent = '✓'; setDot(names[j], 'done'); }
        else if (j === i) { el.className = 'step active'; num.textContent = j + 1; setDot(names[j], 'active'); }
        else { el.className = 'step'; num.textContent = j + 1; }
    }
}

function setDot(name, cls) { document.getElementById('d-' + name).className = 'dot ' + cls; }
function setDots(cls) { ['ceo','research','dev','mkt','support'].forEach(n => setDot(n, cls)); }

// Render results
function render(d) {
    document.getElementById('bar').style.width = '100%';
    document.getElementById('pct').textContent = '100%';
    for (let i = 0; i < 5; i++) {
        const el = document.getElementById('s' + i);
        el.className = 'step done';
        el.querySelector('.step-num').textContent = '✓';
    }
    setDots('done');
    setTimeout(() => {
        document.getElementById('progress').classList.remove('show');
        document.getElementById('results-section').classList.add('show');
    }, 800);

    const map = {
        ceo_strategy: 'ceo', market_research: 'research',
        product_development: 'dev', marketing_plan: 'mkt', customer_support: 'support'
    };
    for (const [k, v] of Object.entries(map)) {
        const el = document.getElementById('c-' + v);
        if (el) el.innerHTML = md(d[k] || 'No data.');
    }
    if (d.full_report) document.getElementById('full-report').innerHTML = md(d.full_report);
    toast('All 5 agents finished!', 'ok');
}

// Tabs
function tab(name, btn) {
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    btn.classList.add('active');
    document.getElementById('p-' + name).classList.add('active');
}

// Download
function dl(key) {
    const el = document.getElementById('c-' + key);
    if (!el || el.textContent === '—') { toast('No content yet', 'info'); return; }
    const names = { ceo: 'ceo_strategy', research: 'market_research', dev: 'product_development', mkt: 'marketing_plan', support: 'customer_support' };
    const blob = new Blob([el.innerText], { type: 'text/markdown' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = (names[key] || key) + '.md';
    a.click();
    toast('Downloaded!', 'ok');
}

// Full report toggle
function toggleFull() {
    document.getElementById('full-report').classList.toggle('show');
}

// Reset
function reset() {
    jobId = null; data = {};
    if (poll) clearInterval(poll);
    document.getElementById('results-section').classList.remove('show');
    document.getElementById('progress').classList.remove('show');
    document.getElementById('input-card').style.display = '';
    document.getElementById('idea').value = '';
    setDots('idle');
    resetBtn();
    document.getElementById('bar').style.width = '0%';
    document.getElementById('pct').textContent = '0%';
    for (let i = 0; i < 5; i++) {
        const el = document.getElementById('s' + i);
        el.className = 'step';
        el.querySelector('.step-num').textContent = i + 1;
    }
    ['ceo','research','dev','mkt','support'].forEach(k => {
        document.getElementById('c-' + k).textContent = '—';
    });
    document.getElementById('full-report').innerHTML = '';
    document.getElementById('full-report').classList.remove('show');
}

function resetBtn() {
    const btn = document.getElementById('go');
    btn.disabled = false; btn.textContent = '🚀 Launch Company';
}

// Markdown renderer with table support
function md(t) {
    if (!t) return '';

    // Parse tables FIRST (before escaping)
    const lines = t.split('\n');
    let html = '';
    let inTable = false;
    let tableRows = [];

    for (let i = 0; i < lines.length; i++) {
        const line = lines[i].trim();

        // Detect table row: starts and ends with | or has | separators
        if (line.match(/^\|(.+)\|$/)) {
            // Skip separator rows like | --- | --- |
            if (line.match(/^\|[\s\-:]+\|$/)) continue;
            tableRows.push(line);
            inTable = true;
        } else {
            // If we were in a table, flush it
            if (inTable && tableRows.length > 0) {
                html += buildTable(tableRows);
                tableRows = [];
                inTable = false;
            }
            // Process regular line
            html += processLine(line) + '\n';
        }
    }
    // Flush any remaining table
    if (tableRows.length > 0) html += buildTable(tableRows);

    return html;
}

function buildTable(rows) {
    let h = '<table class="md-table"><thead><tr>';
    // First row = header
    const headerCells = rows[0].split('|').filter(c => c.trim());
    headerCells.forEach(c => { h += '<th>' + esc(c.trim()) + '</th>'; });
    h += '</tr></thead><tbody>';
    // Remaining rows = body
    for (let i = 1; i < rows.length; i++) {
        h += '<tr>';
        const cells = rows[i].split('|').filter(c => c.trim());
        cells.forEach(c => { h += '<td>' + esc(c.trim()) + '</td>'; });
        h += '</tr>';
    }
    h += '</tbody></table>';
    return h;
}

function esc(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function processLine(line) {
    let s = esc(line);
    // Headers
    s = s.replace(/^### (.+)$/, '<h3>$1</h3>');
    s = s.replace(/^## (.+)$/, '<h2>$1</h2>');
    s = s.replace(/^# (.+)$/, '<h1>$1</h1>');
    // Bold & italic
    s = s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    s = s.replace(/\*(.+?)\*/g, '<em>$1</em>');
    // Inline code
    s = s.replace(/`([^`]+)`/g, '<code>$1</code>');
    // List items
    s = s.replace(/^- (.+)$/, '<li>$1</li>');
    s = s.replace(/^\d+\. (.+)$/, '<li>$1</li>');
    // Horizontal rule
    s = s.replace(/^---$/, '<hr style="border:none;border-top:1px solid #e5e7eb;margin:12px 0">');
    // Empty line = paragraph break
    if (s === '') s = '<br>';
    return s;
}

// Toast
function toast(msg, type) {
    const box = document.getElementById('toasts');
    const el = document.createElement('div');
    el.className = 'toast ' + (type || 'info');
    el.textContent = msg;
    box.appendChild(el);
    setTimeout(() => { el.style.opacity = '0'; setTimeout(() => el.remove(), 300); }, 3500);
}

// Ctrl+Enter
document.addEventListener('keydown', e => {
    if (e.ctrlKey && e.key === 'Enter') launch();
});
