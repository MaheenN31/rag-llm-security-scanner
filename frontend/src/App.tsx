import { Route, Routes } from "react-router";
import { Layout } from "./components/Layout";
import { AttackReplay } from "./pages/AttackReplay";
import { Dashboard } from "./pages/Dashboard";
import { Findings } from "./pages/Findings";
import { Reports } from "./pages/Reports";
import { Settings } from "./pages/Settings";

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route index element={<Dashboard />} />
        <Route path="/findings" element={<Findings />} />
        <Route path="/attack-replay" element={<AttackReplay />} />
        <Route path="/reports" element={<Reports />} />
        <Route path="/settings" element={<Settings />} />
      </Route>
    </Routes>
  );
}