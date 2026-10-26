import { Link } from "react-router-dom";

export default function NotFound() {
  return (
    <section>
      <h1>Seite nicht gefunden</h1>
      <p>Diese Adresse gibt es nicht.</p>
      <Link to="/">Zurück zur Startseite</Link>
    </section>
  );
}
