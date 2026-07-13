export function AttackReplay() {
    return (
      <div className="space-y-6">
        <section>
          <p className="text-sm font-semibold uppercase tracking-[0.3em] text-blue-400">
            Attack Replay
          </p>
          <h2 className="mt-3 text-3xl font-bold text-white">
            Probe Execution Details
          </h2>
          <p className="mt-3 text-slate-400">
            This page will show the input prompt, retrieved chunks, model
            response, and detector result for each security probe.
          </p>
        </section>
  
        <div className="grid gap-4 lg:grid-cols-2">
          <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-5">
            <h3 className="font-semibold text-white">Probe Input</h3>
            <pre className="mt-4 whitespace-pre-wrap rounded-xl bg-slate-950 p-4 text-sm text-slate-300">
              Placeholder probe input will appear here.
            </pre>
          </div>
  
          <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-5">
            <h3 className="font-semibold text-white">Model Response</h3>
            <pre className="mt-4 whitespace-pre-wrap rounded-xl bg-slate-950 p-4 text-sm text-slate-300">
              Placeholder model response will appear here.
            </pre>
          </div>
        </div>
      </div>
    );
  }