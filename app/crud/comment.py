from sqlalchemy.orm import Session
from app.models.comment import Comment
from app.schemas.comment import CommentCreate, CommentUpdate

def create_comment(db: Session, report_id: int, user_id: int, comment_in: CommentCreate):
    comment = Comment(report_id=report_id, user_id=user_id, text=comment_in.text)
    db.add(comment)
    db.commit()
    db.refresh(comment)
    return comment

def get_comment(db: Session, comment_id: int):
    return db.query(Comment).filter(Comment.id == comment_id).first()

def get_comments_for_report(db: Session, report_id: int):
    return db.query(Comment).filter(Comment.report_id == report_id).all()

def update_comment(db: Session, comment_id: int, comment_in: CommentUpdate):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment:
        comment.text = comment_in.text
        db.commit()
        db.refresh(comment)
    return comment

def delete_comment(db: Session, comment_id: int):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if comment:
        db.delete(comment)
        db.commit()
    return comment
