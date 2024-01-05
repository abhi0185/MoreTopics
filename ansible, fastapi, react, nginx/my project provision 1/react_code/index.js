import ReactDOM from 'react-dom/client';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import App from './App';
import Region from './pages/Region.js';
import Environment from './pages/Environment.js';

export default function Main() {
  return (
    <BrowserRouter>
      <Routes>
          <Route path="/" element={<App />} />
          <Route path="regions" element={<Region />} />
          <Route path="environments" element={<Environment />} />
      </Routes>
    </BrowserRouter>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Main />);
