# chatbot-memory-llmAgent-RAG-pdf-mcp-python-ai-projects
AI Chatbots | LLM Applications | AI Agents | RAG Pipelines | Local LLMs | Document Intelligence | MCP Automation | LangChain Projects

## 🛠️ Included Modules
### 1. 🤖 AI Chatbot with Persistent Memory
* **Tech Stack:** Python, Google Gemini 2.5 Flash, JSON, Google GenAI SDK
* **Overview:** A conversational AI chatbot that maintains long-term conversation history by storing previous interactions locally in a JSON file and automatically restoring them when the application starts.
* **Key Features:**
  * **Persistent Memory:** Saves both user prompts and AI responses into a local JSON file and reloads them in future sessions.
  * **Automatic Context Loading:** Initializes every new chat using previously stored conversation history.
  * **Continuous Conversation:** Maintains context across multiple executions without requiring a database.
  * **Simple CLI Interface:** Lightweight command-line chatbot powered by Gemini 2.5 Flash.

---

### 3. 📄 AI PDF Extraction Pipeline
* **Tech Stack:** Google Gemini 2.5 Flash, PyPDFium2, Pillow (PIL), JSON
* **Overview:** An intelligent document extraction pipeline that converts scanned PDFs into high-resolution images, enhances image quality, and extracts structured JSON using a multimodal LLM.
* **Key Features:**
  * **High-Resolution Rendering:** Converts every PDF page into 300 DPI images for improved recognition.
  * **Image Enhancement:** Applies grayscale conversion, contrast enhancement, and sharpening before LLM processing.
  * **Structured AI Extraction:** Uses Gemini vision capabilities to accurately extract handwritten fields, printed text, and checkbox selections.
  * **JSON Output:** Returns clean structured JSON ready for downstream automation or processing.

---

### 4. 🔍 AI Research Agent
* **Tech Stack:** LangChain, Google Gemini 2.5 Flash, DuckDuckGo Search, Pydantic, Python
* **Overview:** An autonomous research assistant capable of searching the web, collecting information, organizing results into structured JSON, and saving research reports locally.
* **Key Features:**
  * **Tool Calling Agent:** Allows the LLM to intelligently decide when external web search is required.
  * **Integrated Web Search:** Retrieves current information using DuckDuckGo through LangChain tools.
  * **Structured Responses:** Formats research into Topic, Summary, Sources, and Tools Used.
  * **Research Export:** Automatically saves research findings into timestamped local text files.

---

### 5. 🧠 Local LLM RAG Application
* **Tech Stack:** Ollama, Llama 3, MXBAI Embeddings, ChromaDB, LangChain
* **Overview:** A Retrieval-Augmented Generation (RAG) application that answers user questions using local documents without relying on cloud APIs.
* **Key Features:**
  * **100% Local AI:** Runs entirely using locally installed Ollama language and embedding models.
  * **Vector Database:** Converts CSV documents into embeddings and stores them inside ChromaDB.
  * **Semantic Retrieval:** Retrieves the most relevant document chunks before generating responses.
  * **Private Knowledge Base:** Enables question answering over custom datasets while keeping data on the local machine.

---

### 6. ⚙️ MCP AI Agent Automation
* **Tech Stack:** Claude Desktop, Model Context Protocol (MCP), Playwright, MySQL, REST API, Excel, Filesystem
* **Overview:** A multi-tool AI agent that leverages the Model Context Protocol (MCP) to orchestrate browser automation, databases, APIs, Excel, and local file operations from a single natural language prompt.
* **Key Features:**
  * **Browser Automation:** Performs end-to-end web interactions using Playwright MCP.
  * **Database Integration:** Reads and writes data directly from MySQL databases.
  * **REST API Execution:** Understands API contracts and performs validation requests automatically.
  * **File & Excel Automation:** Creates, updates, and manages Excel files and local documents through MCP tools.
  * **Multi-Tool Agent Workflow:** Coordinates several external tools to complete complex real-world automation tasks from one user instruction.
