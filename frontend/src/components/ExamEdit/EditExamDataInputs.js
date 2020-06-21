import React from "react";
import EditFormInput from "./EditFormInput";
import { Form } from "react-bootstrap";
class EditExamDataInputs extends React.Component {
  /**
   * Component that represents all inputs that the user has to manually enter or type
   */
  render() {
    return (
      <>
        <EditFormInput
          controlId="examName"
          name="name"
          label="Nombre del Examen"
          input_type="text"
          placeholder="Ingresar Nombre del Examen"
          value={this.props.data.name}
          handleChange={this.props.handleInputChange}
        />
        <EditFormInput
          controlId="dueDate"
          name="dueDate"
          label="Fecha de realización"
          input_type="date"
          placeholder="dd/mm/aaaa"
          value={this.props.data.dueDate}
          handleChange={this.props.handleInputChange}
        />
        <EditFormInput
          controlId="startTime"
          name="startTime"
          label="Hora de Inicio"
          input_type="time"
          placeholder="HH:MM"
          value={this.props.data.startTime}
          handleChange={this.props.handleInputChange}
        />
        <EditFormInput
          controlId="endTime"
          name="endTime"
          label="endTime"
          input_type="time"
          placeholder="HH:MM"
          value={this.props.data.endTime}
          handleChange={this.props.handleInputChange}
        />
        <EditFormInput
          controlId="teacher"
          name="teacher"
          label="Nombre profesor/a"
          input_type="text"
          placeholder="Nombre del profesor/a"
          value={this.props.data.teacher}
          handleChange={this.props.handleInputChange}
        />
        <EditFormInput
          controlId="courseName"
          name="courseName"
          label="Nombre del curso"
          input_type="text"
          placeholder="Nombre del curso"
          value={this.props.data.courseName}
          handleChange={this.props.handleInputChange}
        />
        <EditFormInput
          controlId="courseCode"
          name="courseCode"
          label="Codigo del curso"
          input_type="text"
          placeholder="Codigo del curso"
          value={this.props.data.courseCode}
          handleChange={this.props.handleInputChange}
        />
        <EditFormInput
          controlId="university"
          name="university"
          label="Universidad"
          input_type="text"
          placeholder="Nombre de la Universidad"
          value={this.props.data.university}
          handleChange={this.props.handleInputChange}
        />

        <Form.Group controlId="language">
          <Form.Label>Idioma del examen</Form.Label>
          <Form.Control
            onChange={this.props.handleInputChange}
            name="language"
            as="select"
            value={this.props.data.language}
          >
            <option value="EN">Ingles</option>
            <option value="ES">Español</option>
          </Form.Control>
        </Form.Group>
      </>
    );
  }
}
export default EditExamDataInputs;
