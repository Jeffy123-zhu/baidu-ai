class MediDocApp {
    constructor() {
        this.uploadArea = document.getElementById('uploadArea');
        this.fileInput = document.getElementById('fileInput');
        this.processBtn = document.getElementById('processBtn');
        this.resultArea = document.getElementById('resultArea');
        this.currentFile = null;
        
        this.initEventListeners();
    }
    
    initEventListeners() {
        // Upload area click
        this.uploadArea.addEventListener('click', () => {
            this.fileInput.click();
        });
        
        // File input change
        this.fileInput.addEventListener('change', (e) => {
            this.handleFileSelect(e.target.files[0]);
        });
        
        // Drag and drop
        this.uploadArea.addEventListener('dragover', (e) => {
            e.preventDefault();
            this.uploadArea.classList.add('dragover');
        });
        
        this.uploadArea.addEventListener('dragleave', () => {
            this.uploadArea.classList.remove('dragover');
        });
        
        this.uploadArea.addEventListener('drop', (e) => {
            e.preventDefault();
            this.uploadArea.classList.remove('dragover');
            this.handleFileSelect(e.dataTransfer.files[0]);
        });
        
        // Process button
        this.processBtn.addEventListener('click', () => {
            this.processDocument();
        });
        
        // Tab switching
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', (e) => {
                this.switchTab(e.target.dataset.tab);
            });
        });
    }
    
    handleFileSelect(file) {
        if (!file) return;
        
        const validTypes = ['application/pdf', 'image/jpeg', 'image/png', 'image/jpg'];
        if (!validTypes.includes(file.type)) {
            alert('Please upload a PDF or image file');
            return;
        }
        
        this.currentFile = file;
        this.uploadArea.innerHTML = `
            <div class="upload-icon">✓</div>
            <p><strong>${file.name}</strong></p>
            <p>${(file.size / 1024 / 1024).toFixed(2)} MB</p>
        `;
        this.processBtn.disabled = false;
    }
    
    async processDocument() {
        if (!this.currentFile) return;
        
        this.processBtn.disabled = true;
        this.showLoading();
        
        // Simulate processing stages
        await this.simulateOCR();
        await this.simulateAgentAnalysis();
        await this.generateReport();
        
        this.processBtn.disabled = false;
    }
    
    showLoading() {
        this.resultArea.innerHTML = `
            <div class="loading">
                <div class="spinner"></div>
                <p>Processing document...</p>
            </div>
        `;
    }
    
    async simulateOCR() {
        this.resultArea.innerHTML = `
            <h3>Stage 1: OCR Processing</h3>
            <div class="agent-status active">
                <div class="agent-icon">📄</div>
                <div class="agent-info">
                    <h4>PaddleOCR-VL</h4>
                    <p>Extracting text from document...</p>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: 0%"></div>
                    </div>
                </div>
            </div>
        `;
        
        await this.animateProgress('.progress-fill', 100, 800);
        
        this.resultArea.querySelector('.agent-status').classList.remove('active');
        this.resultArea.querySelector('.agent-status').classList.add('complete');
        this.resultArea.querySelector('.agent-status p').textContent = 'Text extracted successfully (96% confidence)';
    }
    
    async simulateAgentAnalysis() {
        const agents = [
            { name: 'Document Analyzer', icon: '🔍', task: 'Structuring medical data...' },
            { name: 'Cardiology Agent', icon: '❤️', task: 'Analyzing cardiovascular indicators...' },
            { name: 'Radiology Agent', icon: '🔬', task: 'Reviewing imaging reports...' },
            { name: 'Medication Agent', icon: '💊', task: 'Checking drug interactions...' }
        ];
        
        this.resultArea.innerHTML += '<h3>Stage 2: Multi-Agent Analysis</h3>';
        
        for (const agent of agents) {
            const agentHtml = `
                <div class="agent-status active">
                    <div class="agent-icon">${agent.icon}</div>
                    <div class="agent-info">
                        <h4>${agent.name}</h4>
                        <p>${agent.task}</p>
                        <div class="progress-bar">
                            <div class="progress-fill" style="width: 0%"></div>
                        </div>
                    </div>
                </div>
            `;
            this.resultArea.innerHTML += agentHtml;
            
            const lastAgent = this.resultArea.querySelector('.agent-status:last-child');
            await this.animateProgress(lastAgent.querySelector('.progress-fill'), 100, 1000);
            
            lastAgent.classList.remove('active');
            lastAgent.classList.add('complete');
            lastAgent.querySelector('p').textContent = 'Analysis complete';
        }
    }
    
    async generateReport() {
        await new Promise(resolve => setTimeout(resolve, 500));
        
        this.resultArea.innerHTML = `
            <h3>Analysis Complete</h3>
            
            <div class="stats">
                <div class="stat-card">
                    <h3>1.8s</h3>
                    <p>Processing Time</p>
                </div>
                <div class="stat-card">
                    <h3>96%</h3>
                    <p>OCR Confidence</p>
                </div>
                <div class="stat-card">
                    <h3>94%</h3>
                    <p>Agent Consensus</p>
                </div>
            </div>
            
            <div class="tabs">
                <button class="tab active" data-tab="professional">Professional Report</button>
                <button class="tab" data-tab="patient">Patient-Friendly</button>
            </div>
            
            <div class="tab-content active" id="professional">
                <div class="report">
                    <h3>Diagnostic Report</h3>
                    
                    <div class="report-section">
                        <h4>Patient Information</h4>
                        <p>Male, 65 years old</p>
                        <p>Chief Complaint: Chest discomfort for 3 days</p>
                    </div>
                    
                    <div class="report-section">
                        <h4>Multi-Agent Analysis</h4>
                        <p><strong>Cardiology:</strong> Possible coronary artery disease. Recommend coronary angiography.</p>
                        <p><strong>Radiology:</strong> Left ventricular hypertrophy detected on imaging.</p>
                        <p><strong>Medication:</strong> Recommend Aspirin 100mg + Atorvastatin 20mg.</p>
                    </div>
                    
                    <div class="report-section">
                        <h4>Consensus Diagnosis</h4>
                        <p>
                            <span class="badge badge-warning">Probable CAD</span>
                            <span class="badge badge-info">Hypertension Stage 3</span>
                        </p>
                        <p>Confidence: 94%</p>
                    </div>
                    
                    <div class="report-section">
                        <h4>Recommendations</h4>
                        <ul>
                            <li>Complete coronary CT examination</li>
                            <li>Adjust antihypertensive medication</li>
                            <li>Add antiplatelet therapy</li>
                            <li>Follow-up in 2 weeks</li>
                        </ul>
                    </div>
                </div>
            </div>
            
            <div class="tab-content" id="patient">
                <div class="report">
                    <h3>Your Health Report</h3>
                    
                    <div class="report-section">
                        <h4>What We Found</h4>
                        <p>Based on your examination, your heart may not be getting enough blood supply. This is called coronary artery disease.</p>
                    </div>
                    
                    <div class="report-section">
                        <h4>What You Need to Do</h4>
                        <ol>
                            <li>Schedule a heart scan (coronary CT)</li>
                            <li>Take prescribed medications daily</li>
                            <li>Follow a low-salt, low-fat diet</li>
                            <li>Avoid strenuous exercise</li>
                            <li>Come back for check-up in 2 weeks</li>
                        </ol>
                    </div>
                    
                    <div class="report-section">
                        <h4>Questions?</h4>
                        <p>Please contact your healthcare provider if you have any concerns or if symptoms worsen.</p>
                    </div>
                </div>
            </div>
        `;
        
        // Re-attach tab listeners
        document.querySelectorAll('.tab').forEach(tab => {
            tab.addEventListener('click', (e) => {
                this.switchTab(e.target.dataset.tab);
            });
        });
    }
    
    switchTab(tabName) {
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
        
        document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');
        document.getElementById(tabName).classList.add('active');
    }
    
    animateProgress(element, targetWidth, duration) {
        return new Promise(resolve => {
            let start = null;
            const animate = (timestamp) => {
                if (!start) start = timestamp;
                const progress = timestamp - start;
                const percentage = Math.min((progress / duration) * targetWidth, targetWidth);
                
                if (typeof element === 'string') {
                    document.querySelector(element).style.width = percentage + '%';
                } else {
                    element.style.width = percentage + '%';
                }
                
                if (progress < duration) {
                    requestAnimationFrame(animate);
                } else {
                    resolve();
                }
            };
            requestAnimationFrame(animate);
        });
    }
}

// Initialize app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new MediDocApp();
});
