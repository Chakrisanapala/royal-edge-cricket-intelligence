import React, { useEffect, useState } from 'react';
import { api } from '../services/api';
import { 
  ResponsiveContainer, 
  AreaChart, 
  Area, 
  XAxis, 
  YAxis, 
  Tooltip, 
  PieChart, 
  Pie, 
  Cell, 
  BarChart, 
  Bar, 
  CartesianGrid 
} from 'recharts';
import { Activity, ShieldCheck, Flame, Info } from 'lucide-react';

export const PressureIntelligence: React.FC = () => {
  const [data, setData] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.getPressureSummary().then(res => {
      setData(res);
      setLoading(false);
    });
  }, []);

  if (loading || !data) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-[#EB107E]"></div>
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Overview Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col justify-between">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Leverage Definition</span>
            <Activity className="w-4 h-4 text-[#7BD0FF]" />
          </div>
          <div className="mt-4">
            <div className="text-2xl font-bold text-white">Match Pressure (P_t)</div>
            <p className="text-xs text-gray-300 mt-1 leading-relaxed">
              Dynamically derived from balls remaining (<span className="text-[#FABC4D] font-mono">B_t</span>), wickets in hand (<span className="text-[#FABC4D] font-mono">10 - W_t</span>), and required run rate (<span className="text-[#FABC4D] font-mono">RRR_t</span>).
            </p>
          </div>
        </div>

        <div className="bg-[#0D1C2D] border border-[#EB107E]/30 rounded-xl p-5 flex flex-col justify-between relative overflow-hidden">
          <div className="absolute top-0 right-0 w-24 h-24 bg-[#EB107E]/10 rounded-full blur-xl pointer-events-none"></div>
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-[#EB107E] uppercase tracking-wider">High Pressure Threshold</span>
            <Flame className="w-4 h-4 text-[#EB107E]" />
          </div>
          <div className="mt-4">
            <div className="text-3xl font-extrabold text-[#EB107E] font-mono">LEI ≥ 1.50</div>
            <p className="text-xs text-gray-300 mt-1">
              Top 22.86% of competitive balls (45,951 deliveries). Extreme leverage triggers at <span className="text-[#FABC4D] font-mono">LEI ≥ 2.50</span>.
            </p>
          </div>
        </div>

        <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col justify-between">
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Knockout Match Weight</span>
            <ShieldCheck className="w-4 h-4 text-[#FABC4D]" />
          </div>
          <div className="mt-4">
            <div className="text-3xl font-extrabold text-[#FABC4D] font-mono">1.15× Multiplier</div>
            <p className="text-xs text-gray-300 mt-1">
              Applied universally to playoff, semi-final, and elimination matches across IPL and ICC T20 World Cups.
            </p>
          </div>
        </div>
      </div>

      {/* Main Charts Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
        {/* Leverage Timeline Chart */}
        <div className="lg:col-span-8 bg-[#0D1C2D] border border-white/10 rounded-xl p-5">
          <div className="flex items-center justify-between mb-4">
            <div>
              <h3 className="text-sm font-bold text-white uppercase tracking-wider">
                Average Match Leverage by Over (Overs 1–20)
              </h3>
              <p className="text-xs text-gray-400">Progression of average pressure index as overs elapse</p>
            </div>
            <span className="text-[11px] px-2.5 py-1 rounded bg-[#EB107E]/20 text-[#EB107E] font-mono font-semibold">
              Peak: Over 20 (2.68)
            </span>
          </div>

          <div className="h-72 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={data.leverage_timeline} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="pressureGradient" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#EB107E" stopOpacity={0.8}/>
                    <stop offset="95%" stopColor="#EB107E" stopOpacity={0.0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" stroke="#1C2B3C" />
                <XAxis dataKey="over" stroke="#94A3B8" fontSize={11} tickFormatter={(v) => `Over ${v}`} />
                <YAxis stroke="#94A3B8" fontSize={11} domain={[0.5, 3.0]} />
                <Tooltip 
                  contentStyle={{ backgroundColor: '#0D1C2D', borderColor: '#334155', borderRadius: '8px', fontSize: '12px' }}
                  labelFormatter={(v) => `Over ${v}`}
                  formatter={(value: any) => [`${value} LEI`, 'Average Leverage']}
                />
                <Area type="monotone" dataKey="avg_pressure" stroke="#EB107E" strokeWidth={2.5} fillOpacity={1} fill="url(#pressureGradient)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>

          <div className="mt-4 pt-3 border-t border-white/5 flex flex-wrap items-center justify-between gap-2 text-xs text-gray-400">
            <div className="flex items-center gap-2">
              <span className="w-2.5 h-2.5 rounded-full bg-[#7BD0FF]"></span> Powerplay (0.85–1.05)
            </div>
            <div className="flex items-center gap-2">
              <span className="w-2.5 h-2.5 rounded-full bg-[#FABC4D]"></span> Middle Overs (1.15–1.45)
            </div>
            <div className="flex items-center gap-2">
              <span className="w-2.5 h-2.5 rounded-full bg-[#EB107E]"></span> Death Overs (1.82–2.68)
            </div>
          </div>
        </div>

        {/* Leverage Distribution Donut */}
        <div className="lg:col-span-4 bg-[#0D1C2D] border border-white/10 rounded-xl p-5 flex flex-col justify-between">
          <div>
            <h3 className="text-sm font-bold text-white uppercase tracking-wider mb-1">
              Leverage Classification
            </h3>
            <p className="text-xs text-gray-400 mb-4">Ball volume by pressure tier</p>

            <div className="h-52 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <PieChart>
                  <Pie
                    data={data.distribution}
                    dataKey="deliveries"
                    nameKey="name"
                    cx="50%"
                    cy="50%"
                    innerRadius={55}
                    outerRadius={80}
                    paddingAngle={3}
                  >
                    {data.distribution.map((entry: any, index: number) => (
                      <Cell key={`cell-${index}`} fill={entry.color} />
                    ))}
                  </Pie>
                  <Tooltip 
                    contentStyle={{ backgroundColor: '#0D1C2D', borderColor: '#334155', borderRadius: '8px', fontSize: '11px' }}
                    formatter={(val: any) => [Number(val).toLocaleString(), 'Balls']}
                  />
                </PieChart>
              </ResponsiveContainer>
            </div>

            <div className="space-y-2 mt-2">
              {data.distribution.map((d: any) => (
                <div key={d.name} className="flex items-center justify-between text-xs">
                  <div className="flex items-center gap-2">
                    <span className="w-2.5 h-2.5 rounded-sm" style={{ backgroundColor: d.color }}></span>
                    <span className="text-gray-300 truncate max-w-[170px]">{d.name}</span>
                  </div>
                  <span className="font-mono font-bold text-white">{d.pct}%</span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Phase Breakdown Comparison */}
      <div className="bg-[#0D1C2D] border border-white/10 rounded-xl p-5">
        <h3 className="text-sm font-bold text-white uppercase tracking-wider mb-4">
          High-Pressure Concentration Across Match Phases
        </h3>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {data.phase_distribution.map((phase: any) => (
            <div key={phase.phase} className="bg-[#122131] border border-white/5 rounded-lg p-4">
              <div className="text-xs font-bold text-gray-300">{phase.phase}</div>
              <div className="text-2xl font-extrabold text-white font-mono mt-2">{phase.high_pressure_pct}%</div>
              <div className="text-xs text-gray-400 mt-1">
                {phase.high_pressure_balls.toLocaleString()} high-pressure / {phase.total_balls.toLocaleString()} total
              </div>
              <div className="w-full bg-[#051424] h-2 rounded-full mt-3 overflow-hidden">
                <div 
                  className="bg-gradient-to-r from-[#7BD0FF] to-[#EB107E] h-full rounded-full"
                  style={{ width: `${phase.high_pressure_pct}%` }}
                ></div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Methodological Context Box */}
      <div className="bg-[#051424] border border-white/10 rounded-xl p-4 flex items-start gap-3 text-xs text-gray-400">
        <Info className="w-5 h-5 text-[#7BD0FF] shrink-0 mt-0.5" />
        <div>
          <span className="font-bold text-white">Mathematical Pressure Formula: </span>
          In the second innings, <span className="font-mono text-gray-300">P_2nd = 0.50 * (RRR_t / CRR_req) + 0.35 * (10 / (10 - W_t)) + 0.15 * (120 / B_t)</span>. 
          Batters and bowlers are evaluated exclusively during balls where <span className="font-mono text-gray-300">P_t ≥ 1.50</span> to measure true resilience under fire.
        </div>
      </div>
    </div>
  );
};

