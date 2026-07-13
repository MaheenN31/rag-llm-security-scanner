export function Reports() {
    return (
      <div className="space-y-6">
        <section>
          <p className="text-sm font-semibold uppercase tracking-[0.3em] text-blue-400">
            Reports
          </p>
          <h2 className="mt-3 text-3xl font-bold text-white">Scan Reports</h2>
          <p className="mt-3 text-slate-400">
            JSON and HTML reports will be available here after the scanner report
            generator is implemented.
          </p>
        </section>
  
        <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-6">
          <h3 className="text-lg font-semibold text-white">Latest Report</h3>
          <p className="mt-3 text-sm text-slate-400">
            No scan report generated yet.
          </p>
        </div>
      </div>
    );
  }