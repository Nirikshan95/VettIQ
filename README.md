# VettIQ - Startup Idea Validation Tool

A comprehensive AI-powered platform that validates startup ideas through intelligent market analysis, competitor research, risk assessment, and strategic advice. Built with FastAPI backend and Streamlit frontend, VettIQ uses LangGraph workflows and advanced language models to provide data-driven insights for entrepreneurs.

## 🚀 Features

- **AI-Powered Market Analysis**: Deep market insights using DeepSeek-V3 language model
- **Competitive Intelligence**: Automated competitor research and positioning analysis  
- **Risk Assessment**: Multi-dimensional risk evaluation across market, technical, operational, regulatory, and financial factors
- **Strategic Advisory**: Go/No-Go recommendations with actionable next steps
- **Web Search Integration**: Real-time market data through DuckDuckGo search
- **Workflow Orchestration**: LangGraph-powered agent coordination for comprehensive analysis
- **User-Friendly Interface**: Clean Streamlit web interface for easy interaction

## 🏗️ Architecture

VettIQ follows a modular microservices architecture with clear separation of concerns:

```
├── main.py                     # FastAPI backend server
├── app.py                      # Streamlit frontend application
├── config.py                   # Configuration and model parameters
├── graphs/
│   └── workflow.py            # LangGraph workflow orchestration
├── nodes/                     # Analysis agents
│   ├── market_analyst.py      # Market analysis agent
│   ├── competitor_analysis.py # Competitor research agent
│   ├── risk_assessor.py       # Risk assessment agent
│   └── advisor.py             # Strategic advisor agent
├── state/
│   └── agent_state.py         # Shared state management
├── models/
│   └── chat_model.py          # Hugging Face model configuration
├── tools/
│   └── web_search_tool.py     # DuckDuckGo search integration
└── prompts/                   # Agent-specific prompts
    ├── market_analyst.txt
    ├── competitor_analyst_prompt.txt
    ├── risk_assessor.txt
    └── advisor.txt
```

## 📋 Prerequisites

- **Python 3.11+**
- **Hugging Face API Token** (for DeepSeek-V3 model access)
- **Internet connection** for web search functionality

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd vettiq
```

### 2. Set Up Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory:
```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token_here
```

**To obtain a Hugging Face API token:**
1. Visit [Hugging Face](https://huggingface.co/)
2. Create an account or log in
3. Navigate to Settings → Access Tokens
4. Create a new token with appropriate permissions

## 🚀 Usage

VettIQ requires running both the backend API and frontend interface:

### Method 1: Manual Startup (Recommended for Development)

**Terminal 1 - Start the FastAPI Backend:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Terminal 2 - Start the Streamlit Frontend:**
```bash
streamlit run app.py
```

### Method 2: Production Deployment
```bash
# Backend (production mode)
uvicorn main:app --host 0.0.0.0 --port 8000

# Frontend (in separate terminal)
streamlit run app.py --server.port 8501
```

### 3. Access the Application
- **Frontend Interface**: http://localhost:8501
- **API Documentation**: http://localhost:8000/docs
- **API Health Check**: http://localhost:8000

### 4. Validate Your Startup Idea
1. Open the Streamlit interface in your browser
2. Enter your startup idea in the text area
3. Click "Validate" to initiate the analysis
4. Review the comprehensive validation report including:
   - Market analysis and opportunities
   - Competitive landscape assessment
   - Risk evaluation and mitigation strategies  
   - Strategic recommendations and next steps

## ⚙️ Configuration

Customize the analysis behavior in `config.py`:

```python
# Model Configuration
REPO_ID = "deepseek-ai/DeepSeek-V3-0324"  # Language model
TEMPERATURE = 0.7                          # Response creativity (0-1)
MAX_NEW_TOKENS = 512                      # Maximum response length

# API Configuration  
BASE_URL = "http://localhost:8000/"       # Backend API endpoint
```

## 🔄 How It Works

VettIQ employs a sophisticated multi-agent workflow:

1. **Input Processing**: User submits startup idea through Streamlit interface
2. **Market Analysis**: AI agent researches market size, trends, and opportunities
3. **Competitor Research**: Automated competitive intelligence gathering
4. **Risk Assessment**: Multi-dimensional risk evaluation across key categories
5. **Strategic Advisory**: Final recommendations with actionable insights
6. **Report Generation**: Comprehensive validation report delivered to user

Each agent leverages web search capabilities and specialized prompts to ensure thorough, data-driven analysis.

## 📦 Dependencies

### Core Framework
- **FastAPI**: High-performance API backend
- **Streamlit**: Interactive web frontend
- **LangGraph**: Workflow orchestration
- **LangChain Community**: Agent tools and integrations

### AI & ML
- **langchain-huggingface**: Hugging Face model integration
- **DeepSeek-V3**: Advanced language model for analysis

### Search & Data
- **duckduckgo-search**: Web search functionality
- **Pydantic**: Data validation and parsing

## 🔧 API Endpoints

### POST /validate
Validates a startup idea through comprehensive analysis.

**Request Body:**
```json
{
  "startup_idea": "Your startup idea description"
}
```

**Response:**
```json
{
  "startup_idea": "Original idea",
  "market_analysis": "Market insights and opportunities",
  "competition_analysis": "Competitive landscape assessment", 
  "risk_assessment": "Risk factors and mitigation strategies",
  "advisor_recommendations": "Go/No-Go/Conditional Go",
  "advice": "Strategic recommendations and next steps"
}
```

## 🚨 Limitations & Considerations

- **API Dependencies**: Relies on Hugging Face and DuckDuckGo services
- **Rate Limits**: Free tier API usage may have limitations
- **Search Quality**: Analysis quality depends on available web content
- **Response Time**: Initial model loading may cause delays
- **Data Privacy**: Ensure sensitive business ideas are handled appropriately

## 🛠️ Troubleshooting

### Common Issues

**"Unable to connect to the VettIQ API"**
- Ensure FastAPI backend is running on port 8000
- Check firewall settings and port availability
- Verify BASE_URL configuration in config.py

**"Authentication Error" with Hugging Face**
- Verify HUGGINGFACEHUB_API_TOKEN in .env file
- Ensure token has appropriate model access permissions
- Check token validity on Hugging Face platform

**Slow Response Times**
- Free tier models may have longer loading times
- Consider upgrading to paid Hugging Face plan
- Monitor network connectivity for web search operations

**No Search Results**
- Verify internet connectivity
- Try alternative keyword variations
- Check DuckDuckGo service availability

### Debug Mode
Monitor console output from both FastAPI and Streamlit terminals for detailed error logging and agent decision tracking.

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **[LangGraph](https://langchain-ai.github.io/langgraph/)** for workflow orchestration
- **[Hugging Face](https://huggingface.co/)** for language model infrastructure
- **[FastAPI](https://fastapi.tiangolo.com/)** for high-performance API framework
- **[Streamlit](https://streamlit.io/)** for rapid frontend development
- **[DuckDuckGo](https://duckduckgo.com/)** for privacy-focused search functionality

## 🔮 Future Enhancements

- [ ] **Multi-Company Analysis**: Batch validation of multiple startup ideas
- [ ] **Sentiment Analysis**: Market sentiment tracking and analysis
- [ ] **Financial Modeling**: Revenue projections and funding recommendations
- [ ] **Industry Templates**: Specialized validation frameworks by sector
- [ ] **Export Functionality**: PDF/Word report generation
- [ ] **Collaboration Features**: Team-based validation workflows
- [ ] **Historical Tracking**: Progress monitoring and idea evolution
- [ ] **Integration APIs**: Connect with business planning tools
- [ ] **Advanced Visualizations**: Interactive charts and market maps
- [ ] **Localization**: Multi-language support for global markets

---

**Ready to validate your next big idea?** 🚀

For support, feature requests, or contributions, please visit our [GitHub Issues](../../issues) page.