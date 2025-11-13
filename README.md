# COMMONS LEDGER

**Open-source, self-hostable financial tooling for microfinance, SACCOs, and SMEs**

## Mission

Provide **cost-free**, open-source financial tooling that converts everyday SME activity (invoices, receipts, purchase orders) into verifiable credit opportunities and liquidity, without vendor lock-in or paid API dependence.

## Core Features

- ✅ **Simple accounting & invoicing** — Invoice management, payment tracking, expense management
- 📸 **Invoice capture (OCR)** — Snap receipts/invoices; auto-extract using Tesseract + OpenCV
- 📊 **Cashflow forecasting** — Prophet/NeuralProphet-based predictions
- 💰 **Community invoice financing** — P2P tranche marketplace for invoice liquidity
- 🎯 **Open-source credit scoring** — LightGBM + SHAP explainability
- 🔐 **Attestation & provenance** — Signed attestations with optional IPFS hashing
- 🔍 **Batch underwriting wizard** — Configurable micro-underwriting rules
- 🆔 **KYC-lite** — Document capture + OCR comparisons
- 📱 **Offline-first PWA** — Queue uploads in the field, sync when online
- 👨‍💼 **Admin dashboard** — Approve tranches, manage liquidity, export audits

## Tech Stack (100% Open Source)

### Frontend
- **Next.js 14** (React) as PWA
- **Tailwind CSS** for styling
- **IndexedDB** for offline queue
- **TensorFlow.js** for on-device inference

### Backend
- **FastAPI** (Python 3.11+) — Async, lightweight
- **PostgreSQL** — Primary database
- **Redis** — Cache & queue
- **MinIO** — S3-compatible object storage
- **Celery + RQ** — Background tasks

### ML & Data Science
- **Tesseract + OpenCV** — OCR
- **Prophet / NeuralProphet** — Time series forecasting
- **LightGBM + scikit-learn** — Credit models
- **SHAP** — Model explainability
- **Hugging Face Transformers** — Field extraction

### Security & Auth
- **JWT** — Token-based authentication
- **Let's Encrypt** — Free TLS
- **pgcrypto** — Database encryption

### Optional
- **IPFS** — Immutable attestation storage
- **Prometheus + Grafana** — Monitoring

## Quick Start

### Prerequisites
- Docker & Docker Compose
- Node.js 18+ (for local frontend development)
- Python 3.11+ (for local backend development)

### One-Command Deploy

```bash
docker-compose up -d
```

This starts:
- PostgreSQL on port 5432
- Redis on port 6379
- MinIO on port 9000 (console: 9001)
- FastAPI backend on port 8000
- Next.js frontend on port 3000

### Access
- **Frontend**: http://localhost:3000
- **API docs**: http://localhost:8000/docs
- **MinIO console**: http://localhost:9001

## Project Structure

```
commons-ledger/
├── backend/               # FastAPI application
│   ├── app/
│   │   ├── api/          # API endpoints
│   │   ├── core/         # Config, security, deps
│   │   ├── db/           # Database models & migrations
│   │   ├── ml/           # ML models & pipelines
│   │   ├── ocr/          # OCR processing
│   │   └── services/     # Business logic
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/             # Next.js PWA
│   ├── src/
│   │   ├── app/         # App router pages
│   │   ├── components/  # React components
│   │   ├── lib/         # Utilities & API client
│   │   └── hooks/       # Custom React hooks
│   ├── public/
│   ├── package.json
│   └── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

## Development Setup

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Database Migrations

```bash
cd backend
alembic upgrade head
```

## Configuration

Copy `.env.example` to `.env` and configure:

```env
# Database
DATABASE_URL=postgresql://commons:password@localhost:5432/commons_ledger

# Redis
REDIS_URL=redis://localhost:6379/0

# MinIO
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin

# JWT
SECRET_KEY=your-secret-key-here

# ML Models
MODEL_PATH=/models
```

## MVP Roadmap (6 Weeks)

- **Week 1**: Infrastructure (auth, DB, file storage) ✅
- **Week 2**: Invoice capture & OCR 🚧
- **Week 3**: Accounting & invoicing
- **Week 4**: Tranche marketplace
- **Week 5**: Credit scoring & forecasting
- **Week 6**: Attestation & pilot deployment

## API Overview

### Core Endpoints

```
POST   /api/auth/login
POST   /api/auth/register
GET    /api/users/me

POST   /api/invoices
GET    /api/invoices/:id
POST   /api/invoices/:id/ocr
PUT    /api/invoices/:id
DELETE /api/invoices/:id

POST   /api/invoices/:id/tranches
GET    /api/tranches
POST   /api/tranches/:id/pledge

POST   /api/attestations
GET    /api/attestations/:id

GET    /api/forecast/:org_id
GET    /api/score/:entity_id
```

## Security Considerations

⚠️ **Important**: This system enables financing. Review local lending laws before facilitating payouts.

- Store PII encrypted at rest
- Use RBAC for all sensitive operations
- Implement audit logging
- Regular security audits
- GDPR-compliant data export/erase flows

## Legal & Compliance

- KYC-lite is not a full compliance solution
- For regulated lending, partner with licensed institutions
- Provide legal templates for operators
- Review local data protection requirements

## Deployment

### Production Checklist

- [ ] Configure TLS with Let's Encrypt
- [ ] Set strong SECRET_KEY and database passwords
- [ ] Enable database encryption (pgcrypto)
- [ ] Configure backup schedules
- [ ] Set up monitoring (Prometheus/Grafana)
- [ ] Review firewall rules
- [ ] Configure log rotation
- [ ] Set resource limits in docker-compose

### Hosting Options

- **Self-hosted**: Your own server
- **VPS**: DigitalOcean, Hetzner, Linode ($5-20/month)
- **On-premise**: For MFIs with data sovereignty requirements

## Contributing

We welcome contributions! This project is designed for:
- Microfinance institutions
- SACCOs and credit unions
- SME ecosystems
- Financial inclusion advocates

### Areas for Contribution
- Additional OCR languages
- ML model improvements
- Mobile-optimized UI
- Integration adapters (payment gateways, accounting software)
- Documentation & translations

## License

**MIT License** — Use freely, modify, self-host. No vendor lock-in.

## Support & Community

- **Documentation**: [docs/](./docs/)
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions

## Acknowledgments

Built with open-source tools:
- FastAPI, Next.js, PostgreSQL, Redis, MinIO
- Tesseract, OpenCV, Prophet, LightGBM, scikit-learn
- SHAP, Hugging Face Transformers

---

**Built for financial inclusion. Owned by the commons.**
