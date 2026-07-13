import { NavLink, Outlet } from "react-router";

const navItems = [
  { label: "Overview", path: "/" },
  { label: "Findings", path: "/findings" },
  { label: "Attack Replay", path: "/attack-replay" },
  { label: "Reports", path: "/reports" },
  { label: "Settings", path: "/settings" },
];

export function Layout() {
  return (
    <div className="min-h-screen text-slate-100">
      <aside className="fixed left-0 top-0 hidden h-screen w-72 border-r border-slate-800 bg-slate-950/80 p-6 backdrop-blur lg:block">
        <div className="mb-10">
          <p className="text-sm font-semibold uppercase tracking-[0.3em] text-blue-400">
            RAGShield
          </p>
          <h1 className="mt-3 text-2xl font-bold text-white">
            LLM Security Scanner
          </h1>
          <p className="mt-3 text-sm leading-6 text-slate-400">
            Defensive testing dashboard for RAG prompt injection, leakage, and
            retrieval risks.
          </p>
        </div>

        <nav className="space-y-2">
          {navItems.map((item) => (
            <NavLink
              key={item.path}
              to={item.path}
              end={item.path === "/"}
              className={({ isActive }) =>
                [
                  "block rounded-xl px-4 py-3 text-sm font-medium transition",
                  isActive
                    ? "bg-blue-500 text-white shadow-lg shadow-blue-500/20"
                    : "text-slate-300 hover:bg-slate-900 hover:text-white",
                ].join(" ")
              }
            >
              {item.label}
            </NavLink>
          ))}
        </nav>
      </aside>

      <main className="lg:pl-72">
        <div className="border-b border-slate-800 bg-slate-950/70 px-6 py-4 backdrop-blur lg:hidden">
          <p className="text-sm font-semibold uppercase tracking-[0.25em] text-blue-400">
            RAGShield
          </p>
          <h1 className="mt-1 text-xl font-bold">LLM Security Scanner</h1>
        </div>

        <div className="mx-auto max-w-7xl px-6 py-8">
          <Outlet />
        </div>
      </main>
    </div>
  );
}