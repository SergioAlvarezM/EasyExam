import React from "react";
import { Form } from "react-bootstrap";
import AddImage from "./AddImage";
class Statement extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <>
        <Form.Group controlId="statement">
          <Form.Label>Enunciado:</Form.Label>
          <Form.Control
            onChange={this.props.handleChange}
            name="statement_content"
            type="text"
            as="textarea"
            placeholder="Escribe aquí el enunciado de la pregunta. Puedes usar latex."
            rows="3"
          />
        </Form.Group>
        <AddImage />
      </>
    );
  }
}
export default Statement;
