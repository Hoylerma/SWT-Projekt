import { Link, Route, Routes } from "react-router-dom";
import Home from "./pages/Home.jsx";
import Rezepte from "./pages/Rezepte.jsx";
import NotFound from "./pages/NotFound.jsx";

export default function App() {
  return (
    <>
      <header className="kopf">
        <strong>WG Cook</strong>
        <nav>
          <Link to="/">Start</Link>
          <Link to="/rezepte">Rezepte</Link>
        </nav>
      </header>
      <main>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/rezepte" element={<Rezepte />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
    </>
  );
}
