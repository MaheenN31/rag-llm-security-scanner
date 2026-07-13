export function Settings() {
    return (
      <div className="space-y-6">
        <section>
          <p className="text-sm font-semibold uppercase tracking-[0.3em] text-blue-400">
            Settings
          </p>
          <h2 className="mt-3 text-3xl font-bold text-white">Scanner Settings</h2>
          <p className="mt-3 text-slate-400">
            Target URL, model provider, probe count, and scanner options will be
            configured here in later phases.
          </p>
        </section>
  
        <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
          <h3 className="text-lg font-semibold text-white">Target API</h3>
          <p className="mt-3 text-sm text-slate-400">
            Current default backend: http://127.0.0.1:8000
          </p>
        </div>
      </div>
    );
  }