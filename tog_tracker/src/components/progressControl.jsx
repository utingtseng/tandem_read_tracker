import { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import eOS from "../assets/empireofstorm.jpg";
import tOD from "../assets/towerofdawn.jpg";
import kOA from "../assets/kingdomofash.jpg";
const API_URL = "http://127.0.0.1:5000";

const ProgressControl = () => {
  const [books, setBooks] = useState();
  const bookOrder = ["prev", "curr", "next"];

  useEffect(() => {
    fetch(`${API_URL}/tandem/current_chapter`)
      .then((res) => {
        console.log("Response status:", res.status);
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        console.log("Response data:", data);
        setBooks(data);
      })
      .catch((error) => {
        console.error("Fetch error:", error);
      });
  }, []);

  return (
    <>
      {books
        ? bookOrder.map((order) => {
            const book = books[order];
            return (
              <BookSection order={order} book={book} setBooks={setBooks} />
            );
          })
        : null}
    </>
  );
};
export default ProgressControl;

const BookSection = ({ book, order, setBooks }) => {
  const sectionName = {
    curr: "Currently reading",
    prev: "Just finished",
    next: "Coming up next",
  };

  const images = {
    "Tower of Dawn": tOD,
    "Empire of Storms": eOS,
    Completed: kOA,
  };

  const [newComment, setNewComment] = useState("");

  const handleMarkComplete = () => {
    fetch(`${API_URL}/tandem/complete/${book.section_id}`)
      .then((res) => {
        console.log("Response status:", res.status);
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        console.log("Response data:", data);
        setBooks(data);
      })
      .catch((error) => {
        console.error("Fetch error:", error);
      });
  };

  const handleAddNewComment = () => {
    fetch(`${API_URL}/tandem/new-comment/${book.section_id}`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ newComment: newComment }),
    })
      .then((res) => {
        console.log("Response status:", res.status);
        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }
        return res.json();
      })
      .then((data) => {
        console.log("Response data:", data);
        setBooks(data);
        setNewComment("");
      })
      .catch((error) => {
        console.error("Fetch error:", error);
      });
  };

  return (
    <div className="book-card">
      <img src={images[book.title]} alt={book.title} className="book-cover" />
      <div className="book-details">
        <h2>{sectionName[order]}</h2>
        <h4>{book.title}</h4>
        <p>
          <strong>Chapters:</strong> {book.chapters}
        </p>
        {book.comments && book.comments.length >= 1 && (
          <p>
            <strong>Comments:</strong>
            <BookComments comments={book.comments} />
          </p>
        )}
        <br></br>
        {order == "curr" ? (
          <>
            <Row>
              <Col>
                <Form.Control
                  type="text"
                  id="addComments"
                  value={newComment}
                  onChange={(e) => {
                    setNewComment(e.target.value);
                  }}
                />
              </Col>
              <Col>
                <Button onClick={handleAddNewComment}>+ Comments</Button>
              </Col>
            </Row>
            <Button onClick={handleMarkComplete}>Mark as completed!</Button>
          </>
        ) : null}
      </div>
    </div>
  );
};

const BookComments = ({ comments }) => {
  return (
    <>
      {comments.map((comment) => {
        return <li>{comment.comments}</li>;
      })}
    </>
  );
};
