export const fields = [
 {id:'interfaces',title:'界面科学',description:'界面の力学、熱力学と微視的構造',groups:[{title:'界面の記述',ids:['young-laplace-coarse-graining','gibbs-to-tolman-gauge-curvature','van-der-waals-diffuse-interface','kirkwood-buff-stress-anisotropy','curvature-dependent-surface-tension']}]},
 {id:'statistical-physics',title:'統計物理',description:'一次元スピン系の相関と応答',groups:[{title:'一般理論',ids:['finite-range-symmetry-comparison']},{title:'最近接模型',ids:['ising-transfer-matrix','clock-chain-nearest-neighbor','xy-chain-nearest-neighbor']},{title:'第二近接模型',ids:['ising-r2-transfer-matrix','clock-chain-second-neighbor','xy-chain-second-neighbor','ising-xy-second-neighbor-comparison']},{title:'不均一系・量子系',ids:['ising-r1-periodic','xxz-chain-quantum']}]},
 {id:'quasicrystals',title:'準結晶',description:'準周期関数、射影法と回折',groups:[{title:'非周期秩序',ids:['quasiperiodic-functions-torus','fibonacci-cut-and-project','quasicrystal-diffraction-fourier-module']}]},
 {id:'mathematics',title:'数学',description:'解析学と特殊関数',groups:[{title:'解析',ids:['asymptotic-analysis-map']},{title:'楕円関数',ids:['elliptic-functions-map','elliptic-factorization','elliptic-unification']}]},
 {id:'economics',title:'経済学',description:'消費者選択、価格競争と商品設計',groups:[{title:'市場理論',ids:['consumer-choice-and-price-formation','nash-bertrand-price-competition','price-quality-joint-choice','multiproduct-competitor-repositioning']}]},
 {id:'culture',title:'文化・その他',description:'作品分析と研究構想',groups:[{title:'研究構想',ids:['anime-vector-analysis']}]},
] as const;
export type FieldId = typeof fields[number]['id'];
export function fieldFor(id:string, explicit?:FieldId) {
 return fields.find(f=>f.id===explicit) ?? fields.find(f=>f.groups.some(g=>(g.ids as readonly string[]).includes(id)));
}
export const revisionDate = (data:{publishedAt:Date;updatedAt?:Date})=>data.updatedAt ?? data.publishedAt;
export const formatDate=(date:Date)=>date.toLocaleDateString('ja-JP',{timeZone:'Asia/Tokyo',year:'numeric',month:'2-digit',day:'2-digit'});
