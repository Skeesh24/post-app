from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.classes.database import get_db
from app.classes.models import User, Vote
from app.classes.oauth2 import get_current_user
from app.classes.schemas.votes import vote_create, vote_response


router = APIRouter(prefix="/votes", tags=["Votes"])


@router.post("", response_model=str, status_code=status.HTTP_201_CREATED)
async def set_vote(vote: vote_create, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    newvote_dict = vote.dict()
    newvote_dict.update({"user_id": user.id})
    dir = newvote_dict.pop("vote_direction")
    message = ""

    # getting by the composite pk!
    old_vote = db.get(Vote, (vote.post_id, user.id))

    if dir == 1:
        if old_vote:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                f"ur vote to this post is already exist")
        new_vote = Vote(**newvote_dict)
        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)
        message = "successfuly voted"
    else:
        if old_vote:
            db.delete(old_vote)
            db.commit()
            message = "ur vote was successfuly deleted"
        else:
            raise HTTPException(status.HTTP_400_BAD_REQUEST,
                                f"ur vote to this post doesn't exist")

    return message
