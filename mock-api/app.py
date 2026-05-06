"""
FastAPI Mock Payment Server
Run with: uvicorn app:app --reload
"""

from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
from models import TransferRequest, TransferResponse

app = FastAPI(
    title="FinPay Payment API",
    description="Mock payment API for testing automation",
    version="1.0.0"
)

# Enable CORS for frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory database (resets on restart)
transfers_db: Dict[str, TransferResponse] = {}


@app.get("/")
def root():
    return {
        "message": "FinPay API is running",
        "endpoints": [
            "GET  /health",
            "POST /api/v1/transfers",
            "GET  /api/v1/transfers",
            "GET  /api/v1/transfers/{id}",
            "DELETE /api/v1/transfers/{id}/cancel"
        ]
    }


@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "FinPay Mock API", "transfers_count": len(transfers_db)}


@app.post("/api/v1/transfers", status_code=status.HTTP_201_CREATED)
def create_transfer(request: TransferRequest) -> TransferResponse:
    
    response = TransferResponse(
        amount=request.amount,
        currency=request.currency,
        recipient=request.recipient
    )
    
    transfers_db[response.id] = response
    
    if request.amount < 10000:
        response.complete()
    
    return response


@app.get("/api/v1/transfers/{transfer_id}")
def get_transfer(transfer_id: str) -> TransferResponse:
    
    if transfer_id not in transfers_db:
        raise HTTPException(
            status_code=404, 
            detail=f"Transfer {transfer_id} not found"
        )
    
    return transfers_db[transfer_id]


@app.get("/api/v1/transfers")
def list_transfers(limit: int = 10, offset: int = 0) -> List[TransferResponse]:
    
    all_transfers = list(transfers_db.values())
    return all_transfers[offset:offset + limit]


@app.delete("/api/v1/transfers/{transfer_id}/cancel")
def cancel_transfer(transfer_id: str):
    
    if transfer_id not in transfers_db:
        raise HTTPException(status_code=404, detail="Transfer not found")
    
    transfer = transfers_db[transfer_id]
    
    if transfer.status != "PENDING":
        raise HTTPException(
            status_code=400, 
            detail=f"Cannot cancel transfer in {transfer.status} status"
        )
    
    transfer.fail()
    return {"message": "Transfer cancelled", "id": transfer_id, "status": "FAILED"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)