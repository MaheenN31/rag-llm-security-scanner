type StatCardProps = {
    label: string;
    value: string | number;
    helper?: string;
  };
  
  export function StatCard({ label, value, helper }: StatCardProps) {
    return (
      <div className="rounded-2xl border border-slate-800 bg-slate-900/70 p-5 shadow-xl shadow-slate-950/20">
        <p className="text-sm font-medium text-slate-400">{label}</p>
        <p className="mt-3 text-3xl font-bold text-white">{value}</p>
        {helper ? <p className="mt-2 text-sm text-slate-500">{helper}</p> : null}
      </div>
    );
  }