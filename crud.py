
from sqlalchemy.orm import Session
import model
import schema


def get_todo_by_todo_id(db: Session, title: str):
    """
    This method will return single movie details based on movie_id
    :param db: database session object
    :param movie_id: movie id only
    :return: data row if exist else None
    """
    return db.query(model.todo_list).filter(model.todo_list.title == title).first()


# def get_user_by_email(db: Session, id: int):
#     return db.query(model.todo_list.filter(model.todo_list.id == id).first()




def get_todo(db: Session, skip: int = 0, limit: int = 100):
    """
    This method will return all movie details which are present in database
    :param db: database session object
    :param skip: the number of rows to skip before including them in the result
    :param limit: to specify the maximum number of results to be returned
    :return: all the row from database
    """
    return db.query(model.todo_list).offset(skip).limit(limit).all()


def add_todo_details_to_db(db: Session, todo: schema.todo_list_add):
    """
    this method will add a new record to database. and perform the commit and refresh operation to db
    :param db: database session object
    :param movie: Object of class schema.MovieAdd
    :return: a dictionary object of the record which has inserted
    """
    mv_details = model.todo_list(
        title=todo.title,
        description = todo.description,
        
    )
    db.add(mv_details)
    db.commit()
    db.refresh(mv_details)
    return mv_details


def update_todo_details(db: Session, sl_id: int, details: schema.Update_todo_list):
    """
    this method will update the database
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :param details: Object of class schema.UpdateMovie
    :return: updated movie record
    """
    db.query(model.todo_list).filter(model.todo_list.id == sl_id).update(vars(details))
    db.commit()
    return db.query(model.todo_list).filter(model.todo_list.id == sl_id).first()


def delete_todo_details_by_id(db: Session, sl_id: int):
    """
    This will delete the record from database based on primary key
    :param db: database session object
    :param sl_id: serial id of record or Primary Key
    :return: None
    """
    try:
        db.query(model.todo_list).filter(model.todo_list.id == sl_id).delete()
        db.commit()
    except Exception as e:
        raise Exception(e)

def get_todo_by_id(db: Session, id: int):
    return db.query(model.todo_list).filter(model.todo_list.id == id).first()        