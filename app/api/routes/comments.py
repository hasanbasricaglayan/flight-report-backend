from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.comment import CommentCreate, CommentOut, CommentUpdate
from app.db.session import get_db
from app.crud.comment import create_comment, get_comment, get_comments_for_report, update_comment, delete_comment
from app.api.deps import get_current_user

router = APIRouter(prefix="/comments", tags=["comments"])

@router.post("/{report_id}", response_model=CommentOut)
def add_comment(report_id: int, comment: CommentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_comment(db, report_id, current_user.id, comment)

@router.get("/{report_id}", response_model=list[CommentOut])
def list_comments(report_id: int, db: Session = Depends(get_db)):
    return get_comments_for_report(db, report_id)

@router.put("/{comment_id}", response_model=CommentOut)
def edit_comment(comment_id: int, comment_update: CommentUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    comment = update_comment(db, comment_id, comment_update)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    return comment

@router.delete("/{comment_id}", response_model=dict)
def remove_comment(comment_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    comment = get_comment(db, comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    if comment.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized")
    delete_comment(db, comment_id)
    return {"detail": "Comment deleted"}
